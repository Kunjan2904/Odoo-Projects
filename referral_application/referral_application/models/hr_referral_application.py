from odoo import models,fields

class HrReferralApplication(models.Model):
    _name = "hr.referral.application"
    _description = "Hr Referral Application"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    referral_name_id = fields.Many2one("hr.employee",string="Referral Name")
    degree_id = fields.Many2one("hr.recruitment.degree",string="Degree")
    department_id = fields.Many2one("hr.job",string="Department")
    expected_salary = fields.Float(string="Expected Salary")
    summary = fields.Text(string="Summary")
    expected_joining_date = fields.Date(string="Expected Joining Date")
    stage = fields.Selection([('draft','Draft'),
                              ('approved','Approved'),
                              ('cancel','Cancelled')],string="Status",default="draft",copy=False)

    def action_approved(self):
        self.write({'stage':'approved'})

    def action_cancel(self):
        self.write({'stage':'cancel'})

    def action_create_application(self):
        pass