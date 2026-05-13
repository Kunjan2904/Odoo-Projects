from odoo import models,api

class ResPartner(models.Model):
    _inherit = "res.partner"

    def name_get(self):
        """ Method For See Customer Name Along With City in Partner id Field in Drop Down"""
        result = []
        for partner in self:
            if partner.parent_id:
                name = str(partner.parent_id.name) +', ' +str(partner.name) + ' [' + str(partner.city) + ']'
            else:
                name = str(partner.name) + ' [' + str(partner.city) + ']'
            result.append((partner.id,name))
        return result
      
    @api.model
    def _name_search(self,name='',args=None,operator='ilike',limit=100, name_get_uid=None):
        """ Method For Search The Particular Customer With City Name """
        if args is None:
            args = []
        domain = args + ['|', ('name', operator, name), ('city', operator, name)]
        return self._search(domain, limit=limit, access_rights_uid=name_get_uid)
