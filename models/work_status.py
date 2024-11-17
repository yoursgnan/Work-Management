# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class WorkStatus(models.Model):
    """
    Class to store type of work
    """
    _name = 'work.status'
    _description = 'Class to store type of work'

    # fields
    sequence = fields.Integer('Sequence')
    name = fields.Char('Name', help='Give some name to your type; for ex: To Do/Doing/Done etc.')
    active = fields.Boolean('Active', help='Enabling this will show this under dropdown in other places.')
    final_stage_bool = fields.Boolean('Final Stage',help='Helps to identify final stage and will set work item progress as 100')