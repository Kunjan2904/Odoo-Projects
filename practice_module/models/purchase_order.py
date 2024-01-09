from odoo import fields,models
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_combine_draft(self):
        # if len(self) <= 1:
        #     # Nothing to merge only one or zero record selected
        #     return

        # vendor = self[0].partner_id  # Check all order not belongs to same vendor
        # if not all(order.partner_id == vendor for order in self):
        #     raise UserError("Not Merge Quotation Because All Not Belongs to Same Vendor")

        # # Create New Order to Merge Quotations
        # merge_order = self.env['purchase.order'].create({
        #     'partner_id':vendor.id
        #     })

        # # Merge Order Lines into the merged order
        # for order in self:
        #     for line in order.order_line:
        #         merge_order.order_line += line

        # # Delete the other quotations except for the merged order
        # for order in self:
        #     if order != merge_order:
        #         order.unlink()


        activate_ids = self._context.get('active_ids')
        first_purchase_id = self.browse(activate_ids[0])
        if len(activate_ids) > 1:
            for rec in activate_ids[1:]:
                if self.browse(rec).partner_id.id != first_purchase_id.partner_id.id:
                    raise UserError("Not Merge Quotation Because Not Belongs to Same Vendor")
                elif self.browse(rec).state != 'purchase' or first_purchase_id.state != 'purchase':
                    raise UserError("Selected Quotation Is Not In Purchase State")
                else:
                    purchase_rec = self.browse(rec)
                    first_purchase_id.write({
                        'order_line': [(4, line.id) for line in purchase_rec.order_line]
                    })
                    purchase_rec.write({'state':'cancel'})
                    purchase_rec.unlink()
        else:
            raise UserError("If you merge quotation please select at lease one more draft.")
