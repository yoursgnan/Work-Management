# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class WorkItemAttachment(models.Model):
    """
    Class to store any attachments related to work item
    """
    _name = 'work.item.attachment'
    _description = "Class to store any attachments related to work item"

    name = fields.Char('Name')
    attachment_type = fields.Selection([
        ('image','Image'),
        ('document','Document'),
    ],'Attachment Type')

    image_binary = fields.Image('Image')
    document_binary = fields.Binary('Document')

    work_item_id = fields.Many2one('work.item','Work Item')