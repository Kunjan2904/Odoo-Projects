{
    
    'name' : 'Referral Application',
    'version' : '15.0.1.0.0',
    'summary' : 'HR Referral Application',
    'author': 'Kunjan Patel',
    'webiste' : 'www.aktiv.software.com',
    'description' : '',
    'category' :  'Technical/Referral Application',

    'depends' : ['hr_recruitment'],
    'data' : [
        "security/security_access_data.xml",
        "security/ir.model.access.csv",
        "views/hr_referral_application_views.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

    'license' : 'LGPL-3',
}

