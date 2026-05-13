from odoo import models,fields,api


class Doctor(models.Model):
	_name = "doctor.doctor"
	_description = "Doctor Information"
	_inherits = {"res.partner" : "doctor_id"}
	_inherit = ['mail.thread', 'mail.activity.mixin']

	# patient_data_ids = fields.One2many("sale.order","doctor_id",string="Patient Data")
	patient_data_ids = fields.One2many("patient.data","doctor_id",string="Patient Data")


	@api.model
	def create(self,vals):
		for record in self:
			if vals.get('name'):
				message = f"The {self.name} Named New Doctor Created."
				self.message_post(body=message)
		return super().create(vals)


	
