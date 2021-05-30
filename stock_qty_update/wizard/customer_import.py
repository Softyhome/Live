from odoo import api,models,fields
from xmlrpc import client as xmlrpclib
import xlrd
import base64
from datetime import datetime,timedelta

class StockImport(models.TransientModel):
    _name = 'customer.export'
    _description = 'Data Export'

    file = fields.Binary('File')
    file_name = fields.Char('Document Name')

    def create_stock_cptwh(self):
        wb = xlrd.open_workbook(file_contents=base64.decodestring(self.file))
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        data = [sheet.row_values(rowx) for rowx in range(1, sheet.nrows)]
        line = []
        product_list = []
        for r in data:
            if r[0]:
                product_rec = self.env['product.product'].search([('default_code', '=', r[0])])
                product_list.append(product_rec.id)
                line.append((0, 0, {
                    'product_id': product_rec.id,
                    'product_qty': r[2],
                    'location_id': self.env['stock.warehouse'].search([('name', '=', 'CPT')], limit=1).lot_stock_id.id,
                }))
        loc = self.env['stock.warehouse'].search([('name', '=', 'CPT')], limit=1).lot_stock_id
        stock_inventory_rec = self.env['stock.inventory'].sudo().create({
            'product_ids': [(6, 0, product_list)],
            'location_ids': [(6, 0, loc.ids)],
            'accounting_date': datetime.now().date() - timedelta(days=38),
            'name': 'CPTWH STOCK ' + str(datetime.now().date() - timedelta(days=38)),
            'line_ids': line
        })
        stock_inventory_rec.action_start()
        stock_inventory_rec.action_validate()

    def create_stock_jhbwh(self):
        wb = xlrd.open_workbook(file_contents=base64.decodestring(self.file))
        sheet = wb.sheet_by_index(1)
        sheet.cell_value(0, 0)
        data = [sheet.row_values(rowx) for rowx in range(1, sheet.nrows)]
        line = []
        product_list = []
        for r in data:
            if r[0]:
                product_rec = self.env['product.product'].search([('default_code', '=', r[0])])
                product_list.append(product_rec.id)
                line.append((0, 0, {
                    'product_id': product_rec.id,
                    'product_qty': r[2],
                    'location_id': self.env['stock.warehouse'].search([('name', '=', 'JHB')], limit=1).lot_stock_id.id,
                }))
        loc = self.env['stock.warehouse'].search([('name', '=', 'JHB')], limit=1).lot_stock_id
        stock_inventory_rec = self.env['stock.inventory'].sudo().create({
            'product_ids': [(6, 0, product_list)],
            'location_ids': [(6, 0, loc.ids)],
            'accounting_date': datetime.now().date() - timedelta(days=38),
            'name': 'JHBWH STOCK ' + str(datetime.now().date() - timedelta(days=38)),
            'line_ids': line
        })
        stock_inventory_rec.action_start()
        stock_inventory_rec.action_validate()
