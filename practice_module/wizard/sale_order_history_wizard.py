from odoo import models,fields

class SaleOrderHistoryWizard(models.TransientModel):
    _name = "sale.order.history.wizard"
    _description = "Sale Order History Wizard"
    # _inherits= {'sale.order.line':'sale_id'}

    product_id = fields.Many2one('product.product')
    name_id = fields.Many2one('sale.order', string="Sale Order")
    unit_price = fields.Float(string='Unit Price')
    quantity = fields.Float(string='Quantity')
    total = fields.Float(string='Total')
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status')
    sale_order_line_id = fields.Many2one('sale.order.line', string='Sale Order Line')

    def action_show_history(self):
        pass

    def delete_wizard(self):
        self.unlink()