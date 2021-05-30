# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def _default_warehouse_id(self):
        # !!! Any change to the default value may have to be repercuted
        # on _init_column() below.
        return False

    warehouse_id = fields.Many2one(
        'stock.warehouse', string='Warehouse',
        required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        default=_default_warehouse_id, check_company=True)

    @api.onchange('company_id')
    def _onchange_company_id(self):
        if self.company_id:
            warehouse_id = self.env['ir.default'].get_model_defaults('sale.order').get('warehouse_id')
            self.warehouse_id = False  # warehouse_id or self.user_id.with_company(self.company_id.id)._get_default_warehouse_id().id

    @api.onchange('user_id')
    def onchange_user_id(self):
        super().onchange_user_id()
        self.warehouse_id = False  # self.user_id.with_company(self.company_id.id)._get_default_warehouse_id().id


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account',
                                          index=True, compute="_compute_analytic_account", store=True, readonly=False,
                                          check_company=True, copy=True,required=True)
