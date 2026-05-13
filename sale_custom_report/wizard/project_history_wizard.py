from odoo import models,fields


class ProjectHistoryWizard(models.TransientModel):
	_name = "project.history.wizard"
	_description = "Project History"

	state_date = fields.Date(string="Start Date")
	end_date = fields.Date(string="End Date")

	def action_show_project_history(self):
		pass