from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Transaksi(models.Model):
    _name = 'protrain.transaksi'
    _description = 'New Description'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    # nama_pembeli = fields.Many2one(comodel_name="res.partner", string='Nama Pembeli')
    # id_member = fields.Char(
    #     compute="_compute_id_member",
    #     string='Id_member',
    #     required=False)
    tgl_transaksi = fields.Datetime(string='Tanggal Transaksi', default=fields.Datetime.now())    
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    dettrans_ids = fields.One2many(
        comodel_name='protrain.dettrans',
        inverse_name='transaksi_id', 
        string='Detail Transaksi')
    
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'),('confirm', 'Confirm'),('done', 'Done'),('cancelled', 'Cancelled')], required=True, readonly=True, default='draft')
    
    # @api.depends('nama_pembeli')
    # def _compute_id_member(self):
    #     for rec in self:
    #         rec.id_member = rec.nama_pembeli.id_member

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('dettrans_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['protrain.dettrans'].search([('transaksi_id','=',rec.id)]).mapped('subtotal'))
            rec.total_bayar = a

    @api.ondelete(at_uninstall=False)
    def _ondelete_transaksi(self):
        if self.filtered(lambda line: line.state != 'draft'): 
            raise ValidationError("Tidak Dapat Menghapus Jika Status BUKAN DRAFT")
        else:
            if self.dettrans_ids:
                a=[]
                for rec in self:
                    a = self.env['protrain.dettrans'].search([('transaksi_id','=',rec.id)])
                    print(a)
                for ob in a:
                    print(str(ob.obat_id.name) + '' + str(ob.qty))
                    ob.obat_id.stok += ob.qty

    def write(self,vals):
        for rec in self:
            a = self.env['protrain.dettrans'].search([('transaksi_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.obat_id.name)+' '+str(data.qty)+' '+str(data.obat_id.stok))
                data.obat_id.stok += data.qty
        record = super(Transaksi,self).write(vals)
        for rec in self:
            b = self.env['protrain.dettrans'].search([('transaksi_id','=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.obat_id.name)+' '+str(databaru.qty)+' '+str(databaru.obat_id.stok))
                    databaru.obat_id.stok -= databaru.qty
                else :
                    pass
        return record

    # @api.constrains('name')
    # def check_nota(self):
    #     for rec in self:
    #         if rec.name == self.name:
    #             raise ValidationError("MASUKAN NOMOR NOTA")
    #         elif rec.name == False:
    #             raise ValidationError("No Nota {} sudah Ada..".format(rec.name))

    _sql_constraints = [
        ('nomor_nota_unik','unique(name)','Nomor Nota Tidak Boleh Sama!')
    ]

class DetTrans(models.Model):
    _name = 'protrain.dettrans'
    _description = 'New Description'
    
    name = fields.Char(string='Nama')
    transaksi_id = fields.Many2one(comodel_name='protrain.transaksi', string='Detail Transaksi')
    obat_id = fields.Many2one(comodel_name='protrain.obat', string='List Obat')
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan','qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan
        
    @api.onchange('obat_id')
    def _onchange_obat_id(self):
        if (self.obat_id.harga):
            self.harga_satuan = self.obat_id.harga

    @api.model
    def create(self,vals):
        record = super(DetTrans,self).create(vals)
        if record.qty:
            self.env['protrain.obat'].search([('id','=',record.obat_id.id)]).write({'stok' : record.obat_id.stok-record.qty})
            return record

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty < 1:
                raise ValidationError("Ingin belanja {} berapa banyak...".format(rec.obat_id.name))
            elif (rec.obat_id.stok < rec.qty):
                raise ValidationError('Stok {} , tidak mencukupi hanya tersedia {}'.format(rec.obat_id.name,rec.obat_id.stok))