# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
from venv import create

from .constants import SEQUENCE_CODE
from odoo import models, fields, api

class WorkItem(models.Model):
    """
    class to store each work item
    """
    _name = 'work.item'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'class to store each work item'

    # fields
    name = fields.Char('Name',default='New')

    title = fields.Char('Title')
    description = fields.Html('Description')

    work_type_id = fields.Many2one('work.type','Type', tracking=True)

    priority_id = fields.Many2one('work.priority','Priority', tracking=True)
    deadline = fields.Date('Deadline', tracking=True)

    parent_ids = fields.Many2many(
        'work.item',
        'work_item_work_item_rel',
        'work_item_id',
        'parent_work_item_id',
        string='Parent',
        tracking=True
    )

    status_id = fields.Many2one('work.status','Status', tracking=True)
    progress = fields.Integer('Progress', tracking=True)

    assignee_id = fields.Many2one('res.users','Assign To', tracking=True)

    attachment_ids = fields.One2many('work.item.attachment','work_item_id','Attachments')

    def default_get(self, fields):
        defaults = super(WorkItem, self).default_get(fields)
        if 'create_date' in fields:
            defaults.update(
                create_date=datetime.date.today(),
                create_uid=self.env.user.id,
            )
        if 'work_type_id' in fields:
            task_type = self.env.ref('work_management.work_type_task')
            defaults.update(work_type_id=task_type.id if task_type else False)
        if 'status_id' in fields:
            first_status = self.env['work.status'].search([('sequence','=',1)])
            if first_status:
                defaults.update(status_id = first_status.id)

        if 'assignee_id' in fields:
            if self.env.context.get('my_work_item'):
                defaults.update(assignee_id = self.env.user.id)

        return defaults

    def name_get(self):
        """
        function to set name for record
        """
        result = [
            (
                work_item.id,
                f'{work_item.name} - {work_item.title}'
            )
            for work_item in self
        ]
        return result


    @api.model
    def create(self,vals):
        if vals.get('name','New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(SEQUENCE_CODE)

        result = super(WorkItem, self).create(vals)
        # generate an email to assignee
        result.generate_email_to_assignee()

        return result

    def generate_email_to_assignee(self):
        """
        function to generate an email to assignee
        """
        email_template = self.env.ref('work_management.mail_template_work_item')
        if email_template:
            email_template.send_mail(self.id, force_send=True)

    def write(self, vals):
        status_id = vals.get('status_id')
        if status_id:
            final_stage = self.env['work.status'].search([('final_stage_bool','=',True)])
            if final_stage:
                if status_id == final_stage.id:

                    # updating parent work item ids
                    for parent_id in self.parent_ids:
                        child_ids = self.env['work.item'].search([('parent_ids','in',[parent_id.id,])])

                        if child_ids:
                            child_ids_progress = [
                                child_id.progress
                                for child_id in child_ids
                            ]
                            # average child progress and setting to parent work item
                            parent_progress = sum(child_ids_progress)/len(child_ids_progress)
                            parent_id.progress = parent_progress

                    # updating current work progress
                    vals.update({
                        'progress': 100,
                    })
                else:
                    vals.update({
                        'progress': 0
                    })


        return super(WorkItem, self).write(vals)


