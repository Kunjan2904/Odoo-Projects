from odoo import models,fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    patient_id = fields.Many2one("patient.patient",string="Patient")

    def action_confirm(self):
        for order in self:
            patient_data_is = self.env['doctor.doctor'].search([('doctor_id','=',order.partner_id.id)])
            patient_data = self.env['patient.data'].create({
                'date': self.date_order,
                'sale_order_id': self.id,
                'doctor_id' : patient_data_is.id,
                'patient_id': self.patient_id.id,
            })
            return super().action_confirm()

    
    # def action_confirm(self):
    #     for record in self:
    #         doctor = self.env['doctor.doctor'].search([('name','=',record.partner_id.name)])
    #         if doctor:
    #             doctor.write({
    #                 'patient_data_ids' : [(4,self.id)]
    #                 })
    #         else:
    #             doctor.create({
    #                 'name':self.partner_id.name,
    #                 'is_doctor':True,
    #                 'patient_data_ids':[(0,0,{
    #                 'partner_id': self.partner_id.id,
    #                 'date_order':self.date_order,
    #                 'patient_id':self.patient_id.id,
    #                 'name':self.name,
    #             })]
    #         })
    #     return super().action_confirm()