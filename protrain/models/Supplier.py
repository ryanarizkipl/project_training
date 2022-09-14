from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'protrain.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat Perusahaan')
    notelp = fields.Char(string='No. Telepon')

    obat_id = fields.Many2many(comodel_name='protrain.obat', string='Obat')