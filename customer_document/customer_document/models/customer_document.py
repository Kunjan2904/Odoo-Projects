from odoo import fields,models,api
from datetime import date,datetime
from odoo.exceptions import UserError
import pytz

class CustomerDocument(models.Model):
    _name = "customer.document"
    _description = "Customer Document"
    _rec_name = "customer_id"

    name = fields.Char(string="Name")
    birth_date = fields.Date(string="Birth Date")
    expiry_date = fields.Date(string="Expiry Date")
    # age = fields.Integer(string="Age",compute="_compute_age",store=True)
    age = fields.Integer(string="Age")
    customer_id = fields.Many2one("res.partner",string="Customer")
    state = fields.Selection([('draft','Draft'),
                              ('approved','Approved'),
                              ('expired','Expired'),
                              ('refused','Refused')],string="Status",default="draft")

    # @api.depends('birth_date')
    # def _compute_age(self):
    #     """ Method For Calculate The Age Based Selected Birth Date """
    #     today = date.today()
    #     for record in self:
    #         if record.birth_date:
    #             record.age = today.year - record.birth_date.year

    @api.constrains('age')
    def _check_age(self):
        """ Method For Check If Age of Customer is Less Than 18 Year """
        for record in self:
            if record.age and record.age < 18:
                raise UserError("The Customer Age Can Not Be Less Than 18 Years.")

    def action_approved(self):
        """ Method For Approve The Customer Document Record """
        self.write({'state':'approved'})

    def action_refused(self):
        """ Method For Refuse The Customer Document Record """
        self.write({'state':'refused'})

    def action_set_to_draft(self):
        """ Method For Set To Draft the Customer Document Record """
        self.write({'state':'draft'})

    def action_calcualte_age(self):
        """ Method For Calculate Age When User Click on Button Customer Age Can Be Calculated """
        today = date.today()
        if self.birth_date:
            self.age = today.year - self.birth_date.year

    @api.model
    def _cron_change_state_to_expire(self):
        """ Cron Job Method For If Expiry Date = Current Date Then Document  
            State Will Be Changed to Expired """
        print('\nself--------------',self)
        for record in self:
            if record.expiry_date and record.expiry_date == fields.Date.today():
                record.write({'state':'expired'})