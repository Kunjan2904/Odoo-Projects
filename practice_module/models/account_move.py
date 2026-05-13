from odoo import models,fields
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = "account.move"


    def action_combine_merge_invoice(self):
        active_ids = self._context.get('active_ids')
        print("\n\n active ids \n\n",active_ids)
        first_invoice_id = self.browse(active_ids[0])
        print("\n\n first Invoice id \n\n",first_invoice_id)

        if len(active_ids) > 1:
            for rec in active_ids[1:]:
                print("\n\n record \n\n",rec)
                if self.browse(rec).partner_id.id != first_invoice_id.partner_id.id:
                    raise UserError("Not Merge Invoice Because Not Belongs to Same Customer")
                elif self.browse(rec).state != 'draft' or first_invoice_id.state != 'draft':
                    raise UserError("Selected Invoice is Not in Draft State")
                else:
                    invoice_rec = self.browse(rec)
                    first_invoice_id.write({
                        'invoice_line_ids' : [(4,line.id) for line in invoice_rec.invoice_line_ids]
                        })
                    # invoice_rec.write({'state':'cancel'})
                    invoice_rec.unlink()
        else:
            raise UserError("if you merge invoice please select at lease one more draft")