{ 
    'name' : 'Purchase Customization',
    'version' : '15.0.1.0.0',
    'summary' : 'Purchase Customization',
    'author': 'Kunjan Patel',
    'webiste' : 'www.aktiv.software.com',
    'description' : '',
    'category' :  'Technical/Purchase Customization',

    'depends' : ['purchase','contacts'],
    'data' : [
        'security/security_access_data.xml',
        'views/purchase_order_view.xml',
        'views/res_partner_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

    'license' : 'LGPL-3',
}

