from odoo import models,fields


class ResConfigSettings(models.TransientModel):
	_inherit = "res.config.settings"

	state = fields.Selection([('quotation_state','Quotation State'),('sale_state','Sale Order State')]
	,config_parameter = "sales_history.state")