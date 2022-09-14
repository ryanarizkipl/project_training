from odoo import models, fields, api

class PartnerXlsx(models.AbstractModel):
    _name = 'report.protrain.report_supplier_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, sup):
        sheet = workbook.add_worksheet('Daftar Supplier')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(2, 0, 'Nama Perusahaan', bold)
        sheet.write(2, 1, 'Alamat', bold)
        sheet.write(2, 2, 'No Telepon', bold)
        sheet.write(2, 3, 'Produk Obat', bold)
        row = 3
        col = 0
        for obj in sup:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.alamat)
            sheet.write(row, col+2, obj.notelp)
            for x in obj.obat_id:
                sheet.write(row, col+3, x.name)
                col += 1
            row += 1