from odoo import models,fields
from odoo.exceptions import UserError

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def action_show_history(self):
        # order_line_products = self.env['sale.order.line'].search([('product_id', '=', self.product_id.id)])

        # product_wizard = self.env['sale.order.history.wizard'].search([
        #     ('product_id', '=', self.product_id.id),
        #     ('name_id', 'in', order_line_products.mapped('order_id.id'))
        # ])
        # main_data = self.env['ir.config_parameter'].search([])
        # for_data = [data.value for data in main_data if 'practice_module.state' in data.key]
        # if for_data:
        #     for_data = for_data[0]
        # else:
        #     raise UserError("Select State From Res Config Setting in Sales")

        # filter_new_product = product_wizard.sale_order_line_id.ids

        # for sale_line in order_line_products:
        #     if sale_line.id not in filter_new_product:
        #         self.env['sale.order.history.wizard'].create({
        #             'product_id': sale_line.product_id.id,
        #             'unit_price': sale_line.price_unit,
        #             'quantity' : sale_line.product_uom_qty,
        #             'name_id': sale_line.order_id.id,
        #             'total': sale_line.price_subtotal,
        #             'state': sale_line.state,
        #             'sale_order_line_id': sale_line.id,
        #         })
        return {
                'name': 'Customer Product Sales History',
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order.history.wizard',
                'view_mode': 'tree',
                'view_id': self.env.ref('practice_module.sale_order_wizard_tree_view').id,
                'target': 'new',
                # 'domain': [('product_id', '=', self.product_id.id),('state', '=', for_data)],
                }

