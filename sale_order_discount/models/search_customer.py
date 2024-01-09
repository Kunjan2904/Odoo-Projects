from odoo import models,fields,api


class SearchCustomer(models.Model):
    _name = "search.customer"
    _description = "Search Customer"
    _rec_name = "customer_id"

    customer_id = fields.Many2one('res.partner',string="Customer")
    mobile = fields.Char(string="Mobile")
    phone = fields.Char(string="Phone")

    @api.onchange('customer_id')
    def _onchange_customer_id(self):
        self.mobile = self.customer_id.mobile
        self.phone = self.customer_id.phone

    def search_customer(self):
        return{
        'type': 'ir.actions.act_window',
        'res_model': 'res.partner',
        'res_id': self.customer_id.id,
        'view_mode': 'form',
        'target': 'current'
        }

    def print_customer(self):
       return self.env.ref('sale_order_discount.action_report_customer').report_action(self.customer_id)
    