# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from openerp import api, fields, models, _
from openerp.exceptions import ValidationError as UserError


class CRMClaim(models.Model):

    _inherit = "crm.claim"

    operating_unit_id = fields.Many2one('operating.unit',
                                        'Default Operating Unit',
                                        default=lambda self:
                                        self.env['res.users'].
                                        operating_unit_default_get(self._uid))

    @api.multi
    @api.constrains('operating_unit_id', 'company_id')
    def _check_company_operating_unit(self):
        for rec in self:
            if rec.company_id and \
                    rec.operating_unit_id and \
                    rec.company_id != rec.operating_unit_id.company_id:
                raise UserError(_('The Company in the Claim and in the \
                 Operating Unit must be the same.'))
