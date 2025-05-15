# -*- coding: utf-8 -*-
{
    'name': "regionalizacion_account",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': "Long description of module's purpose",
    'author': "Bidcom",
    'website': "https://bidcom.com.ar",
    'category': 'Extra Tools',
    'version': '0.1',
    'depends': ['regionalizacion', 'account'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
