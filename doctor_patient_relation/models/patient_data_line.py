from odoo import models,fields

class PatientDataLine(models.Model):
	_name = "patient.data.line"
	_description = "Patient Data Line"
	_inherits = {"sale.order.line":"sale_id"}

	patient_data_id = fields.Many2one("patient.data",string="Patient Data")
