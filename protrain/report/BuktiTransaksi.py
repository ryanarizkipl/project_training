from odoo import models, fields, api
from datetime import timedelta

class PartnerXlsx(models.AbstractModel):
    _name = 'report.protrain.report_transaksi_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, trans):
        sheet = workbook.add_worksheet('Bukti Transaksi')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(2, 0, 'Nomor Nota', bold)
        sheet.write(2, 1, 'Nama Pembeli', bold)
        sheet.write(2, 2, 'Tanggal Transaksi', bold)
        sheet.write(2, 3, 'Total Pembayaran', bold)
        sheet.write(2, 4, 'Status', bold)
        row = 3
        col = 0
        for obj in trans:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.nama_pembeli)
            sheet.write(row, col+2, (obj.tgl_transaksi+timedelta(hours=7)).strftime("%d/%m/%Y, %H:%M:%S"))
            sheet.write(row, col+3, str(obj.total_bayar))
            sheet.write(row, col+4, obj.state)
            row += 1