from odoo import fields,models

class ResPartner(models.Model):
	_inherit = "res.partner"

	def name_get(self):
		print("\n\n>>>>>>>>method called\n\n")
		if self._context.get('default_type') == 'delivery':
			result = []
			for partner in self:
				name = str(partner.name) + ' (' + str(partner.email) + ')'
				result.append((partner.id,name))
			return result
		return super().name_get()