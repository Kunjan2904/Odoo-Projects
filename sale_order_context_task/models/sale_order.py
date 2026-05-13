from odoo import models,fields,api

class SaleOrder(models.Model):
	_inherit = "sale.order"

	# partner_shipping_id = fields.Many2one('res.partner',string="Delivery Address",domain=[('parent_id', '=', 'partner_id')])
	
	@api.onchange('partner_id')
	def _onchange_partner_id(self):
		if self.partner_id:
			domain = [('parent_id', '=', self.partner_id.id)]
			return {'domain': {'partner_shipping_id': domain}}

	# @api.onchange('partner_id')
	# def _onchange_partner_id(self):
	# 	result = self.env['res.partner'].search([('partner_shipping_id','=',self.partner_id.id)])
	# 	return result