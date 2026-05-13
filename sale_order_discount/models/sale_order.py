from odoo import models,fields,api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    discount_applies_to = fields.Selection([('order_line','Order Line'),('global','Global')])
    discount = fields.Float(string="Discount", compute='_compute_discount',store=True)

    discount_method = fields.Selection([('fixed','Fixed'),('percentage','Percentage')])
    discount_amount = fields.Float(string="Discount Amount")


    @api.depends('order_line.discount_amount', 'order_line.discount_method', 'order_line.price_subtotal', 'discount_applies_to','discount_method','discount_amount')
    def _compute_discount(self):
        for order in self:
            discount = 0.0
            value_for_total = order.amount_tax
            value = order.amount_untaxed
            if order.discount_applies_to == 'global':
                if order.discount_method == 'percentage':
                    discount += (order.discount_amount / 100) * value
                elif order.discount_method == 'fixed':
                    discount += order.discount_amount
            else:
                for line in order.order_line:    # For Order Line
                    if line.discount_method == 'percentage':
                        discount += (line.discount_amount / 100) * line.price_subtotal
                    elif line.discount_method == 'fixed':
                        discount += line.discount_amount
            
            value -= discount
            value_for_total += value
            order.discount = discount
            order.amount_untaxed = value
            order.amount_total = value_for_total
