# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Work Management',
    'category': 'Productivity',
    'description': """
Manage your work like a professional
=====================================

The Work Management Tool in Odoo is a comprehensive solution designed to streamline team collaboration, 
optimize task handling, and enhance overall productivity. 
This tool is ideal for managing tasks, projects, and work schedules within organizations of any size.

Key Features
    Task Management:
        - Create, assign, and prioritize tasks effortlessly.
        - Set deadlines and track progress with real-time updates.
    Time Tracking:
        - Log work hours directly within tasks. [ Will be released ]
        - Generate detailed time reports for performance analysis. [ Will be released ]
    Collaboration:
        - Attach documents, images, and other resources to tasks for easy reference.
    Automated Notifications:
        - Receive notifications whenever new work is created for you
        
Who Can Use It?
    The Work Management Tool is designed for:
    
    Project Managers looking to oversee projects from start to finish.
    Teams needing a collaborative environment to manage daily tasks.
    Businesses aiming to track and optimize resource utilization.
    This Odoo-based solution is your ultimate tool to ensure timely deliveries, effective collaboration, and successful project outcomes.
    """,
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/email_template.xml',
        'data/ir_sequence.xml',
        'data/work_priority_data.xml',
        'data/work_status_data.xml',
        'data/work_type_data.xml',
        'views/work_type_views.xml',
        'views/work_status_views.xml',
        'views/work_priority_views.xml',
        'views/work_item_views.xml',
        'views/action_items.xml',
        'views/menu_items.xml',
    ],
    'images': ['static/src/description/banner.gif'],
    'author': 'Gnana Prakash',
    'license': 'OPL-1',
    'installable': True,
    'application': True,
}
