from odoo import models,fields,api


class EmployeeLeave(models.Model):
	_name = "employee.leave"
	_description = "Employee Leave"
	_rec_name = "employee_id"
	_inherit = ['mail.thread','mail.activity.mixin']

	hr_id = fields.Many2one('res.users',string="HR")
	employee_id = fields.Many2one('hr.employee',string="Employee")
	leave_type = fields.Selection([('sick','Sick'),('vacation','Vacation')])
	start_date = fields.Date(string="Start Date",default=fields.date.today())
	end_date = fields.Date(string="End Date")
	total_leave = fields.Integer(string="Total Leave",compute='_compute_total_leave',store=True)
	remaining_leave = fields.Integer(string="Remaining Leave",compute='_compute_remaining_leave',store=True)

	stage = fields.Selection([('new','New'),('approved','Approved'),('rejected','Rejected')],default="new")

	# @api.onchange('employee_id')
	# def _onchange_employee_id(self):
	# 	self.remaining_leave = self.employee_id.available_leave

	@api.depends('start_date','end_date')
	def _compute_total_leave(self):
		for record in self:
			if record.start_date and record.end_date:
				total = (record.end_date - record.start_date).days
				record.total_leave = total + 1
	
	@api.depends('employee_id')
	def _compute_remaining_leave(self):
		for record in self:
			if record.employee_id:
				employee = record.employee_id
				record.remaining_leave = employee.available_leave - record.total_leave
				employee.write({'available_leave':record.remaining_leave})

	def action_approved(self):
		self.write({'stage':'approved'})

	def action_rejected(self):
		self.write({'stage':'rejected'})

	def ranbow_msg(self):
		message = "Hello Rainbow Effect is Open"
		return {
                'effect': {
                    'fadeout': 'slow',
                    'message': message,
                    'type': 'rainbow_man',
                }
            }

