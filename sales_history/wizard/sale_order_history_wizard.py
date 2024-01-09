from odoo import models,fields


class SaleOrderHistoryWizard(models.TransientModel):
	_name = "sale.order.history.wizard"
	_description = "Sale Order History Wizard"

	order_line_ids = fields.Many2many("sale.order.line")
	product_id = fields.Many2one("product.product")
	