from odoo import models, fields, api

class PartnerXlsx(models.AbstractModel):
    _name = 'report.protrain.report_obat_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, obat):
        sheet = workbook.add_worksheet('Daftar Obat')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(2, 0, 'Nama Obat', bold)
        sheet.write(2, 1, 'Harga Obat', bold)
        sheet.write(2, 2, 'Stok', bold)
        sheet.write(2, 3, 'Jenis Obat', bold)
        sheet.write(2, 4, 'Supplier', bold)
        row = 3
        col = 0
        for obj in obat:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, str(obj.harga))
            sheet.write(row, col+2, str(obj.stok))
            for xxx in obj.kelobat_id:
                sheet.write(row, col+3, xxx.name)
            for yyy in obj.supplier_id:
                sheet.write(row, col+4, yyy.name)
                col += 1
            row += 1