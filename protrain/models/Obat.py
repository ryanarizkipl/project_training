from odoo import api, fields, models


class Obat(models.Model):
    _name = 'protrain.obat'
    _description = 'New Description'

    name = fields.Char(string='Nama Obat')
    harga = fields.Integer(string='Harga Obat')
    kelobat_id = fields.Many2one(comodel_name='protrain.kelompokobat',
                                        string='Kelompok Obat',
                                        ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='protrain.supplier', string='Supplier')
    stok = fields.Integer(string='Stok Obat')
    
    
