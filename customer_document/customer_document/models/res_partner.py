from odoo import fields,models

class ResPartner(models.Model):
    _inherit = "res.partner"

    customer_record_count = fields.Integer(compute="_compute_customer_count")

    def _compute_customer_count(self):
        """ Smart Button Method For Count the Total Number of Documents Linked To That Customer """
        for record in self:
            record.customer_record_count = self.env['customer.document'].search_count([('customer_id','=',record.id)])

    def action_customer_document(self):
        action_window = {
            "type" : "ir.actions.act_window",
            "res_model" : "customer.document",
            "name" : "Customer Document",
            "view_mode" : "tree,form",
            "domain" : [('customer_id','=',self.id)]
        }
        return action_window
    