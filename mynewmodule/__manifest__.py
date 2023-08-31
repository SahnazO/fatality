# -*- coding: utf-8 -*-
{
    'name': "Lfinx1",

    'summary': """
       How we love customers""",

    'description': """
       My module purpose is to sale awasome products
    """,

    'author': "lfinx",
    'website': "https://www.lfinx1.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable':'true',
    'application':'true',
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
