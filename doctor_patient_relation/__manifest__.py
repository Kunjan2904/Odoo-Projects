{
	
	'name' : 'Hospital Management',
	'version' : '15.0.0.1.0',
	'summary' : 'Hospital Management Module',
	'author': 'Aktiv Software',
	'webiste' : 'www.aktiv.software.com',
	'description' : '',
	'category' :  'Management/doctor_patient_relation',

	'depends' : ['base','sale_management','contacts'],
	'data' : [
		"security/ir.model.access.csv",
		"views/res_partner_view.xml",
		"views/doctor_doctor_view.xml",
		"views/patient_patient_view.xml",
		"views/product_product_view.xml",
		"views/sale_order_view.xml",
		"views/patient_data_view.xml",
	],
	'demo' : [
		'demo/product_data_demo.xml',
	],

	'installable': True,
	'application': True,
	'auto_install': False,

	'license' : 'LGPL-3',
}

