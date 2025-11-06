# -*- coding: utf-8 -*-
{
    'name': "gestion des employes",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Module de gestion des employes
    """,

    'author': "EROARTA SARL",
    'website': "https://www.eroarta.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Ressources Humaines',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/employe_views.xml',
        'views/templates.xml',
        'views/employee_filter_wizard_views.xml',
        'report/rapport_liste_employe.xml'
    ],
        'installable':True,
        'application':True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}

