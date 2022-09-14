from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_pelanggan = fields.Boolean(string='Is Pelanggan')
    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')