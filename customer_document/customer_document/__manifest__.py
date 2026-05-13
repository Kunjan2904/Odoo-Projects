{
    
    'name' : 'Customer Document Task',
    'version' : '15.0.1.0.0',
    'summary' : 'Customer Discount Practical Task',
    'author': 'Kunjan Patel',
    'webiste' : 'www.aktiv.software.com',
    'description' : '',
    'category' :  'Technical/Customer Document Task',

    'depends' : ['contacts','sale_management'],
    'data' : [
        "security/ir.model.access.csv",
        "views/customer_document_views.xml",
        "views/res_partner_view.xml",
        "data/ir_cron_data.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

    'license' : 'LGPL-3',
}

