from odoo import fields,models

class HrDepartment(models.Model):
	_inherit = "hr.department"

	location_id = fields.Many2one('stock.location', string="Source Location")