# -*- coding: utf-8 -*-
{
    'name': "instituto",

    'summary': """
        El módulo recoge (de manera resumida), la información sobre los alumnos de un Centro
de FP y las empresas en las que están haciendo o han hecho las prácticas de FCT.""",

    'description': """
        El módulo recoge (de manera resumida), la información sobre los alumnos de un Centro
de FP y las empresas en las que están haciendo o han hecho las prácticas de FCT.
    """,

    'author': "Mounir",
    'website': "http://www.mounirzs.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Clase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
