from odoo import models,fields


class CrmLead(models.Model):
	_inherit = "crm.lead"

	# lead_count = fields.Integer(string="Lead Count")

	def lead_count(self):
		return{
			'type':'ir.actions.act_window',
			'res_model':'practice.sale',
			'view_mode':'form',
			# 'target':'current',
		}