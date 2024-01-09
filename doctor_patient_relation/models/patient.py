from odoo import models,fields


class Patient(models.Model):
	_name = "patient.patient"
	_description = "Patient Information"
	_inherits = {"res.partner" : "patient_id"}
	_inherit = ['mail.thread', 'mail.activity.mixin']