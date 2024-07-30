# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': "Hostpital Managements",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/doctor_view.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'wizards/patient_bill_wizard_view.xml',
        'views/hospital_menu.xml',
    ],
    # only loaded in demonstration mode
}

