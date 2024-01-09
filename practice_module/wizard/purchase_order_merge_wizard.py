from odoo import models, api, fields

class PurchaseOrderMerger(models.TransientModel):
    _name = 'purchase.order.merger'

    merge_type = fields.Selection(
        [('Create new order cancel selected','Create new order by merging orders and cancel the selected orders'),
        ('Create new order delete selected','Create new order by merging orders and deleting the selected orders'),
        ('select existing order add other orders and cancel','Select existing order and add other orders to the existing order and cancel others'),
        ('select existing order add other orders and delete','Select existing order and add other orders to the existing order and delete others')],string="Merge Type")

    purchase_type = fields.Many2one("purchase.order",string="Purchase Type")

    def action_merge_purchase_orders(self):
        return{
            'type':'ir.actions.act_window',
            'res_model':'purchase.order.merger',
            'view_mode':'form',
            'target':'new',
        }
    #     # Ensure selected_orders is a valid recordset
    #     selected_orders = self.env['purchase.order'].browse(selected_orders)

    #     if merge_option not in ['A', 'B', 'C', 'D']:
    #         raise Warning(_("Invalid merge option."))

    #     vendor_ids = selected_orders.mapped('partner_id')
    #     if len(vendor_ids) > 1:
    #         raise Warning(_("Selected orders must have the same vendor for merging."))

    #     new_order = None
    #     existing_order = None

    #     if merge_option in ['A', 'B']:
    #         new_order = self.env['purchase.order'].create({
    #             'partner_id': vendor_ids[0].id,
    #             'order_line': [(0, 0, line._convert_to_write(line._cache)) for line in selected_orders.mapped('order_line')]
    #         })

    #     if merge_option in ['C', 'D']:
    #         existing_order = self.env['purchase.order'].search([], limit=1)

    #     if new_order and existing_order:
    #         for order in selected_orders:
    #             existing_order.write({
    #                 'order_line': [(0, 0, line._convert_to_write(line._cache)) for line in order.order_line]
    #             })

    #     if merge_option in ['A', 'C']:
    #         selected_orders.write({'state': 'cancel'})
    #     elif merge_option in ['B', 'D']:
    #         selected_orders.unlink()

    def action_merge_orders(self):
        print("\n\n method called-------------")
       