from odoo import models,fields

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', config_parameter='export_sale_task.state')