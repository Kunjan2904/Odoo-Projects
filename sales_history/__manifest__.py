{ 
    'name' : 'Sales History',
    'version' : '15.0.1.0.0',
    'summary' : 'Sales History',
    'author': 'Kunjan Patel',
    'webiste' : 'www.aktiv.software.com',
    'description' : '',
    'category' :  'Technical/Sales History Task',

    'depends' : ['sale_management'],
    'data' : [
        "security/ir.model.access.csv",
        "views/res_config_setting_view.xml",
        "views/sale_order_line_view.xml",
        "wizard/sale_order_history_wizard_view.xml"
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

    'license' : 'LGPL-3',
}

