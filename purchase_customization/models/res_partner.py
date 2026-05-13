from odoo import models,fields


class ResPartner(models.Model):
	_inherit = "res.partner"

	discount = fields.Float(string="Discount(%)")