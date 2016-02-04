# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import tools
from openerp import fields, models
import openerp.addons.decimal_precision as dp


class AccountEntriesReport(models.Model):
    _inherit = "account.entries.report"

    operating_unit_id = fields.Many2one('operating.unit', 'Operating Unit')

    def _select(self):
        select_str = super(AccountEntriesReport, self)._select()
        select_str += """
            ,l.operating_unit_id as operating_unit_id
        """
        return select_str

    def _from(self):
        from_str = super(AccountEntriesReport, self)._from()
        return from_str

    def _where(self):
        where_str = super(AccountEntriesReport, self)._where()
        return where_str

    def _group_by(self):
        group_by_str = super(AccountEntriesReport, self)._group_by()
        group_by_str += """
            ,l.operating_unit_id
        """
        return group_by_str

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        cr.execute("""CREATE or REPLACE VIEW %s as (
            %s
            %s
            %s
            %s
            )""" % (self._table, self._select(), self._from(), self._where(), self._group_by()))
