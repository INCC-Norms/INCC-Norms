# -*- coding: utf-8 -*-
{
    'name': "Distance des clients",

    'summary': """
        """,

    'description': """
        Ce module permet de définir la distace à laquelle se trouve chaque client
    """,

    'author': "Maimouna Diouf",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Maimouna',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
