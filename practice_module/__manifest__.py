{
    
    'name' : 'Practice Module',
    'version' : '15.0.0.1.0',
    'summary' : 'Practice Module',
    'author': 'Aktiv Software',
    'webiste' : 'www.aktiv.software.com',
    'description' : '',
    'category' :  'Technical/Practice Module',

    'depends' : ['crm','sale_management','stock','purchase','hr'],
    'data' : [
        "security/security_access_data.xml",
        "security/ir.model.access.csv",
        "views/crm_lead_view.xml",
        "views/sale_order_line_view.xml",
        "wizard/sale_order_history_wizard_view.xml",
        "views/practice_sale_view.xml",
        "views/product_product_view.xml",
        "views/hr_employee_view.xml",
        "views/hr_department_view.xml",
        "views/purchase_order_view.xml",
        "views/account_move_view.xml",
        "views/res_user_view.xml",
        "views/res_config_setting_view.xml",
        "wizard/purchase_order_merge_wizard_view.xml"
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

    'license' : 'LGPL-3',
}

