# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class WorkType(models.Model):
    """
    Class to store type of work
    """
    _name = 'work.type'
    _description = 'Class to store type of work'

    # fields
    name = fields.Char('Name', help='Give some name to your type; for ex: Task/Issue/Epic etc.')
    active = fields.Boolean('Active', help='Enabling this will show this under dropdown in other places.')