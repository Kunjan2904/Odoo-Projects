{
	
	'name' : 'Sale Order Context Task',
	'version' : '15.0.0.1.0',
	'summary' : 'Implement Sale Order Context Task',
	'author': 'Aktiv Software',
	'website' : 'www.aktiv.software.com',
	'description' : 'Implement Sale Order Context Task',
	'category' :  'Inheritance/Sale Order Context Task',

	'depends' : ['base','sale_management','stock'],
	'data' : [
		"security/ir.model.access.csv",
		"views/stock_picking_view.xml",
	],
	'demo' : [],

	'installable': True,
	'application': True,
	'auto_install': False,

	'license' : 'LGPL-3',
}
