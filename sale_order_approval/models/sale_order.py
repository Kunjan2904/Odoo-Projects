from odoo import models,fields
from odoo.exceptions import UserError

class SaleOrder(models.Model):
	_inherit = "sale.order"

	state = fields.Selection(selection_add=[('waiting_for_approval','Waiting For Approval')])

	def action_confirm(self):
		# result = super().action_confirm()
		# for order in self:
		# 	if order.amount_total > 10000:
		# 		order.state = "waiting_for_approval"
		# 	else:
		# 		order.state = "sale"
		# return result
		if self.amount_total > 10000:
			self.state = "waiting_for_approval"
		else:
			print("\n\n>>>>>>>>>>Context\n\n",self.env.context,self._context)
			return super().action_confirm()

	def approve_button(self):
		if self.state == "waiting_for_approval":
			raise UserError("Cannot Approve This Order Directly.")

	def action_cancel(self):
	    return super().action_cancel()
		
class SaleOrderLine(models.Model):
	_inherit = "sale.order.line"

	price_unit = fields.Float(string="List Price")