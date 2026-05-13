{
    "name": "Sale Custom Report",
    "version": "16.0.1.0.0",
    "summary": "Sale Report",
    "author": "Kunjan Patel",
    "website": "www.aktiv.software.com",
    "description": "",
    "category": "Technical/Sale Report",
    "depends": ["sale_management","project",'stock'],
    "data": [
        "security/ir.model.access.csv",
        'report/sale_order_report.xml',
        'report/sale_order_templates.xml',
        'views/sale_order_line_view.xml',
        "views/project_project_view.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",

    'assets': {
        'web.assets_backend': [
            '/sale_custom_report/static/src/js/project_tree_extend.js',
            '/sale_custom_report/static/src/xml/project_list_button.xml',
     
        ]
    },
}
