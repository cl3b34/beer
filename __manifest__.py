# -*- coding: utf-8 -*-
{
    'name': "beer",

    'summary': """
        Odoo module to support beer specific reporting in Finland
        Supports Valvira and Tulli reporting""",

    'description': """
         Provide support for beer reporting to Valvira and Tulli in Finland
    """,

    'author': "Head Of Cool",
    'website': "http://www.coolhead.fi",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],
    'application': True,

    # always loaded
    'data': [
        'views/beer_menu.xml',
        'views/beer_form.xml',
        'security/ir.model.access.csv',
        # 'views/views.xml',
        #       'views/product_inherited.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
   # 'demo': [
   #     'demo/demo.xml',
   # ],
}
