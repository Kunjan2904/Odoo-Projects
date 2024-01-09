from odoo import models,fields


class SaleOrderProductHistory(models.Model):
	_name = "sale.order.product.history"
	_description = "Sale Order Product History"

	sale_order_id = fields.Many2one("sale.order",string="Sale Order")
	price_unit = fields.Float(string="Unit Price")
	product_uom_qty = fields.Float(string="Quantity")
	price_subtotal = fields.Float(string="Subtotal")