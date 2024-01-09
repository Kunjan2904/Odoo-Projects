from odoo import models,fields

class HrEmployee(models.Model):
	_inherit = "hr.employee"

	available_leave = fields.Integer(string="Available Leaves")