from odoo import models,fields

class StockPicking(models.Model):
	_inherit = "stock.picking"
	
	shipping_cost = fields.Float(string="Shipping Cost")