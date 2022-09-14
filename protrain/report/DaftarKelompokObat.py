from odoo import models, fields, api

class PartnerXlsx(models.AbstractModel):
    _name = 'report.protrain.report_kelompok_obat_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, kelobat):
        sheet = workbook.add_worksheet('Daftar Kelompok Obat')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(2, 0, 'Nama Jenis Obat', bold)
        sheet.write(2, 1, 'Kode Obat', bold)
        sheet.write(2, 2, 'Nama Satuan Obat', bold)
        sheet.write(2, 3, 'Satuan Obat', bold)
        sheet.write(2, 4, 'Kode Rak', bold)
        sheet.write(2, 5, 'Jumlah Item', bold)
        sheet.write(2, 6, 'Daftar Isi', bold)
        row = 3
        col = 0
        for obj in kelobat:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.kode_obat)
            sheet.write(row, col+2, obj.name2)
            sheet.write(row, col+3, obj.stn_obat)
            sheet.write(row, col+4, obj.kode_rak)
            sheet.write(row, col+5, obj.jml_item)
            sheet.write(row, col+6, obj.daftar)
            # for x in obj.obat_ids:
            #     sheet.write(row, col+4, x.name)
            #     col += 1
            row += 1