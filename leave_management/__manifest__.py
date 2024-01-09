{
    
    'name' : 'Leave Management',
    'version' : '15.0.0.1.0',
    'summary' : 'Leave Management Module',
    'author': 'Kunjan Patel',
    'webiste' : 'www.aktiv.software.com',
    'description' : 'Leave Management Manage Employee Leaves',
    'category' :  'Management/Leave Management',

    'depends' : ['hr'],
    'data' : [
        'security/ir.model.access.csv',
        'views/employee_leave_view.xml',
        'views/hr_employee_view.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

    'license' : 'LGPL-3',
}