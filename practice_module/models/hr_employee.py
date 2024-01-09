from odoo import fields,models

class HrEmployee(models.Model):
	_inherit = "hr.employee"
	
	location_dest_id = fields.Many2one('stock.location', string="Destination Location")

