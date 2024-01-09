from odoo import fields,models,api

class SaleOrderLine(models.Model):
	_inherit = "sale.order.line"

	line_number = fields.Integer(string="No")

	@api.model
	def create(self,vals):
		vals['line_number'] = self.env['ir.sequence'].next_by_code('sale.order.line.sequence') or '/'
		return super(SaleOrderLine,self).create(vals)
