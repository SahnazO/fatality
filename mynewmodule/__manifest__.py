# -*- coding: utf-8 -*-
{
    'name': "Shahnazimo",

    'summary': """
       How we love customers""",

    'description': """
       My module purpose is to sale awasome products
    """,

    'author': "erpgo",
    'website': "https://www.lfinx1.odoo.com",
    #  'images': [
    #     'src/user/static/description/icon.png',
    #     'src/user/static/description/love.png',
    # ],
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/conf_lostreason_views.xml',
        'views/app_menu_views.xml',
        'views/views.xml',
        
        # 'views/templates.xml',
    ],
    'installable':True,
    'application':True,
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
