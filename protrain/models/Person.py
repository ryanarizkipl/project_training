from odoo import api, fields, models


class Person(models.Model):
    _name = 'protrain.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    notelp = fields.Char(string='No. Telepon')

class Apoteker(models.Model):
    _name = 'protrain.apoteker'
    _inherit = 'protrain.person'

    id_apt = fields.Char(string='ID Apoteker')
    
class Kasir(models.Model):
    _name = 'protrain.kasir'
    _inherit = 'protrain.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')
