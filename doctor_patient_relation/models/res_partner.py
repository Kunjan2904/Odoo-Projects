from odoo import fields,models

class ResPartner(models.Model):
	_inherit = "res.partner"

	is_doctor = fields.Boolean(string="Is Doctor?")
	is_patient = fields.Boolean(string="Is Patient?")
	
