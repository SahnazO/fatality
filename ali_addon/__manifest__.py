# -*- coding: utf-8 -*-
{
    'name': "Ali's new module",

    'summary': """
        Training purpose dummy addon""",

    'description': """
        Training purpose dummy addon
    """,

    'author': "ERPGO",
    'website': "https://erpgo.az",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '16.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
}
