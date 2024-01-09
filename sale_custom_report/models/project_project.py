from odoo import fields,models


class ProjectProject(models.Model):
	_inherit = "project.project"

	def action_wizard_open(self):
		return{
			'name':'Show Project History Wizard',
			'type':'ir.actions.act_window',
			'res_model' : 'project.history.wizard',
			'view_mode':'form',
			'target':'new'
		}
