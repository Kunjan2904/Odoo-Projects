from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    demo_name = fields.Char(string="Name")

    def action_confirm(self):
        for order in self:
            for line in order.order_line:
                if line.product_uom_qty <=0 :
                    raise UserError(f"Product Uom Qty Can not be less than zero")
                if line.price_unit <=0 :
                    raise UserError(f"Price Unit Can Not Be a less than Zero")
        return super().action_confirm()

    def test(self):
        return {
            # 'name':'Sale Product History',
            'type':'ir.actions.act_window',
            'res_model':'sale.order.history.wizard',
            'view_mode':'form',
            'target':'new',
            }

class PracticeSale(models.Model):

    _name = "practice.sale"
    _description = "Practice Sale"

    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")

    partner_id = fields.Many2one("res.partner",string="Partners")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    address = fields.Char(string="Address")

    total = fields.Float(compute="_compute_total",inverse="_inverse_total")
    amount = fields.Float()
    name = fields.Char(string="Name")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        self.phone = self.partner_id.phone
        self.email = self.partner_id.email
        # self.address = self.partner_id.street
    
    @api.depends("amount")
    def _compute_total(self):
        for record in self:
            record.total = 2.0 * record.amount

    def _inverse_total(self):
        for record in self:
            record.amount = record.total / 2.0 

    @api.constrains("to_date")
    def _check_to_date(self):
        for record in self:
            if record.to_date < fields.Date.today():
                raise ValidationError("The To Date Cannot be set in the past")

    _sql_constraints = [('name', 'unique(name)', 'Name Should be Unique.')]

    @api.model
    def create(self,vals):
        print("\n\n self \n\n",self)
        print("\n\n values \n\n",vals)
        vals['address'] = "Ahmedabad"
        return super(PracticeSale,self).create(vals)

    def write(self,vals):
        print("\n\n self \n\n",self)
        print("\n\n values \n\n",vals)
        return super(PracticeSale,self).write(vals)

    def search_button(self):
        search = self.env['practice.sale'].search([('address','=','Surat')],limit=3,offset=1,order='id desc')
        print("\n\n search \n\n",search)
        search_count = self.env['practice.sale'].search_count([])
        print("\n\n search_count \n\n",search_count)
        browse_record = self.env['practice.sale'].browse()
        print("\n\n browse \n\n",browse_record)

    company_name = fields.Char(string="Company Name")

    @api.model
    def default_get(self,fields):
        vals = super(PracticeSale,self).default_get(fields)
        vals['company_name'] = "Aktiv Software"
        print("\n\n vals",vals)
        return vals 

    def read_button(self):
        read = self.env['practice.sale'].read()
        print("\n\n read \n\n",read)
        read_search = self.env['practice.sale'].search_read([('name','=','Kunjan')],['name','address'])
        print("\n\nsearch read>>>>>>>>\n\n",read_search)
        read_group = self.env['practice.sale'].read_group(
            domain=[('address', '=', 'Ahmedabad')],
            fields=['name'],
            groupby=['name','address'])
        for read_search in read_group:
          print("\n\nreadgroup>>>>>>>>>>\n\n",read_search)

    def name_get(self):
        result = []
        for partner in self:
            name = str(partner.name) + ' [' + str(partner.address) + ']'
            result.append((partner.id,name))
            print("\n\n result \n\n",result)
        return result

    @api.model
    def _name_search(self,name='',args=None,operator='ilike',limit=100, name_get_uid=None):
        print("\n\n name search called>>>>>\n\n")
        if args is None:
            args = []
        domain = args + ['|', ('email', operator, name), ('name', operator, name)]
        print("\n\n domain \n\n",domain)
        return self._search(domain, limit=limit, access_rights_uid=name_get_uid)
        print("\n\n", self._search(domain, limit=limit, access_rights_uid=name_get_uid))



    



