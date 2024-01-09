from odoo import models,fields

class ProductProduct(models.Model):
	_inherit = "product.product"

	is_medicine = fields.Boolean(string="Is Medicine?")