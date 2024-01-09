from odoo import models,fields

class PatientData(models.Model):
	_name = "patient.data"
	_desciption = "Patient Data"
	_inherit = ["mail.thread","mail.activity.mixin"]
	_rec_name = "patient_id"

	date = fields.Date(string="Date")
	patient_id = fields.Many2one("patient.patient",string="Patient Name")
	sale_order_id = fields.Many2one("sale.order",string="Sale Order")
	doctor_id = fields.Many2one("doctor.doctor",string="Doctor")

	patient_data_line_ids = fields.One2many("patient.data.line","patient_data_id",string="Patient Data Line")