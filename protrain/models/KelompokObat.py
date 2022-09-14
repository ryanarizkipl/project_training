from odoo import api, fields, models


class KelompokObat(models.Model):
    _name = 'protrain.kelompokobat'
    _description = 'New Description'

    name = fields.Selection([('tablet', 'Tablet'),('kapsul', 'Kapsul'),('puyer', 'Puyer'),('cair', 'Cair'),('oles', 'Oles'),('tetes', 'Tetes'),('bubuk', 'Bubuk')], string='Nama Jenis Obat')

    kode_obat = fields.Char(string='Kode Obat')
    @api.onchange('name')
    def _onchange_kode_obat(self):
        if self.name == 'tablet':
            self.kode_obat = 'OBT1'
        elif self.name == 'kapsul':
            self.kode_obat = 'OBT2'
        elif self.name == 'puyer':
            self.kode_obat = 'OBT3'
        elif self.name == 'cair':
            self.kode_obat = 'OBT4'
        elif self.name == 'oles':
            self.kode_obat = 'OBT5'
        elif self.name == 'tetes':
            self.kode_obat = 'OBT6'
        elif self.name == 'bubuk':
            self.kode_obat = 'OBT7'

    name2 = fields.Selection([('botol', 'Botol'),('sachet', 'Sachet')], string='Nama Satuan Obat')

    stn_obat = fields.Char(string='Satuan Obat')
    @api.onchange('name2')
    def _onchange_stn_obat(self):
        if self.name2 == 'botol':
            self.stn_obat = 'ST01'
        elif self.name2 == 'sachet':
            self.stn_obat = 'ST02'

    kode_rak = fields.Char(string='Kode Rak')
    obat_ids = fields.One2many(comodel_name='protrain.obat',
                                inverse_name='kelobat_id',
                                string='Daftar Obat')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('obat_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['protrain.obat'].search([('kelobat_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a

    daftar = fields.Char(string='Daftar isi')