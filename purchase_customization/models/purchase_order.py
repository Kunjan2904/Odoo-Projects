from odoo import models,fields,api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=([('append','Append')]))
    # amount_total_with_discount = fields.Monetary(string='Total with Discount', compute='_compute_total_with_discount', store=True)
    date_planned = fields.Datetime(string='Receipt Date') 

    def action_append(self):
        """ Method For Change State Purchase Order to Append """
        self.update({'state':'append'})

    def action_confirm_append(self):
        """Method For Change State Append To Go Back into the Purchase Order """
        self.update({'state':'purchase'})

    # @api.depends('partner_id', 'partner_id.discount', 'order_line.price_total')
    # def _compute_total_with_discount(self):
    #     for order in self:
    #         discount = order.partner_id.discount / 100.0
    #         order.amount_total_with_discount = sum(line.price_subtotal * (1 - discount) for line in order.order_line)

    @api.depends('order_line.price_total')
    def _amount_all(self):
        """ Method For Calculate Discount on Total Field Of Purchase Order 
        Vendor has discount set on it"""
        result =  super()._amount_all()
        if self.partner_id.discount:
            for order in self:
                order.amount_total -= order.amount_total * order.partner_id.discount / 100 
        return result


#     @api.onchange('partner_id')
#     def _onchange_partner_discount(self):
#         if self.partner_id:
#             self.amount_total = self.partner_id.discount

#     total_discount = fields.Monetary(string="Total Discount",compute="_compute_total_discount",store=True)

#     @api.onchange('order_line')
#     def _onchange_set_discount(self):
#         for order in self.order_line:
#             order.discount = self.partner_id.discount

#     @api.depends('total_discount','order_line.price_subtotal','order_line.discount_amount')
#     def _compute_total_discount(self):
#         for order in self:
#             order.total_discount = sum(order.order_line.mapped('discount_amount'))
            

# class PurchaseOrderLine(models.Model):
#     _inherit = "purchase.order.line"

#     discount =  fields.Float(string="Disc(%)")
#     discount_amount = fields.Float(string="Discount Amount",compute="_compute_discount_amount",store=True)

#     @api.depends('discount_amount','price_subtotal')
#     def _compute_discount_amount(self):
#         for line in self:
#             total = line.price_unit * line.product_uom_qty
#             discount_amount = total * line.discount / 100
#             line.price_subtotal = line.price_subtotal - discount_amount
#             line.order_id.amount_total = sum(line.mapped('price_subtotal'))
#             line.discount_amount = discount_amount