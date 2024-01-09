{
	
	'name' : 'Sale Order Approval',
	'version' : '15.0.0.1.0',
	'summary' : 'Implement Sale Order Approval Task',
	'author': 'Aktiv Software',
	'website' : 'www.aktiv.software.com',
	'description' : 'Implement Sale Order Approval Task',
	'category' :  'Inheritance/Sale Order Approval Task',

	'depends' : ['base','sale_management'],
	'data' : [
		"views/sale_order_view.xml",
	],
	'demo' : [],

	'installable': True,
	'application': True,
	'auto_install': False,

	'license' : 'LGPL-3',
}
