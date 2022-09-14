from odoo import api, fields, models


class BarangDatang(models.TransientModel):
    _name = 'protrain.barangdatang'

    obat_id = fields.Many2one(string='Nama Obat',comodel_name='protrain.obat',required='True')
    jumlah = fields.Integer(string='Jumlah',required='False')

    def button_barang_datang(self):
        for rec in self:
            self.env ['protrain.obat'].search([('id', '=', rec.obat_id.id)]).write({'stok': rec.obat_id.stok + rec.jumlah})
 