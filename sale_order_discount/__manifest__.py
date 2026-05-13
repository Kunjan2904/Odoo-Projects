{
	
	'name' : 'Sale Order Discount',
	'version' : '15.0.0.1.0',
	'summary' : 'Implement Practical Task Sale Order Discount',
	'author': 'Aktiv Software',
	'website' : 'www.aktiv.software.com',
	'description' : '''In This Practical Task Paper Perform Three Different Task 
			Add Global Discount in Sales Order, Select the product category-based product,
			Search Customer.''',
	'category' :  'Paper/Practical Task Paper',

	'depends' : ['base','sale_management','contacts'],
	'data' : [
		"security/ir.model.access.csv",
		"views/sale_order_view.xml",
		"views/search_customer_views.xml",
		"wizard/search_customer_wizard_view.xml",
		"report/customer_report_templates.xml",
		"report/sale_report_templates.xml",
	],
	'demo' : [],

	'installable': True,
	'application': True,
	'auto_install': False,

	'license' : 'LGPL-3',
}
