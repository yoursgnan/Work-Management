# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class WorkPriority(models.Model):
    """
    Class to store priority of work
    """
    _name = 'work.priority'
    _description = 'Class to store priority of work'

    # fields
    name = fields.Char('Name', help='Give some name to your priority; for ex: P1/P2/P3 etc.')
    active = fields.Boolean('Active', help='Enabling this will show this under dropdown in other places.')