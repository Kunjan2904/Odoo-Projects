from odoo import models,fields
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def action_show_history(self):
       
        state = self.env['ir.config_parameter'].get_param('sales_history.state')
        product = self.product_id
        
        if not state:
            raise UserError("Please Select State From Sale Order Settings For Show History")
        elif state == 'quotation_state':
            sale_orders = self.env['sale.order'].search([('state','=','draft')])
        elif state == 'sale_state':
            sale_orders = self.env['sale.order'].search([('state','=','sale')])

        sale_order_lines = sale_orders.mapped('order_line').filtered(lambda a:a.product_id == self.product_id)
        print("\n\n lines>>>>>>>>>>>",sale_order_lines)
        sale_orders = sale_order_lines.mapped('order_id')
        print("\n\n sale_orders >>>>>>>>",sale_orders)

        return {
            'name':'Customer Product Sales History',
            'type':'ir.actions.act_window',
            'res_model':'sale.order.history.wizard',
            'view_mode': 'form',
            'target':'new',
            'context':{
                'default_product_id':self.product_id.id,
                'default_order_line_ids':sale_order_lines.ids
            }
        }

        # line_products = self.search([('product_id','=',self.product_id.id)])
        # print("\n\n line_products>>>>>>",line_products)

        # product_data = self.env['sale.order.history.wizard'].search([('product_id','=',self.product_id.id),('order_line_ids','in',line_products.mapped('order_id'))])
        # print("\n\n product data >>>>>>>",product_data)

        # if get_state:
        #     get_state = get_state[0]
        # else:
        #     raise UserError("Please Select State From Sale Order Settings For Show History")

        # # new_product = product_data.order_id.ids
        # # print("\n\n new_product >>>>>>>",new_product)

        # for sale_line in line_products:
        #     # if sale_line.id not in new_product:
        #     self.env['sale.order.history.wizard'].create({
        #         'product_id':sale_line.product_id.id,
        #         # 'price_unit':sale_line.price_unit,
        #         # 'product_uom_qty':sale_line.product_uom_qty,
        #         # 'order_id':sale_line.order_id.id,
        #         # 'price_subtotal':sale_line.price_subtotal,
        #     })

