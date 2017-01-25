# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError,ValidationError




class Partner(models.Model):
    _inherit = 'res.partner'

    old_code = fields.Char(string="Code client", required=False)
    code = fields.Char(string="Numéro client", required=False)

    @api.multi
    @api.depends('name', 'code')
    def name_get(self):
        result = []
        for partner in self:
            name=partner.name or ''
            if partner.code:
                name = '['+partner.code+']'+name
            result.append((partner.id, name))
        return result

    @api.model
    def create(self, data):
        user = self.env['res.users'].browse(self.env.uid)
        if not user.has_group('partner_wkf.partner_group_user'):
             raise UserError(_("Vous n'avez pas le droit de créer un partenaire"))
        if data['customer']:
            data['code']=self.env['ir.sequence'].next_by_code('customer.sequence') or _('New')
        partner = super(Partner, self.with_context(mail_create_nolog=True)).create(data)
        partner.message_post(body=_('%s a crée le partenaire %s') % (user.name, partner.name))
        return partner

    @api.multi
    def write(self, vals):
        """
         controle user how was made the change
        """
        user = self.env['res.users'].browse(self.env.uid)
        if not user.has_group('partner_wkf.partner_group_manager') :
             raise UserError(_("Vous n'avez pas le droit de modifier la fiche partenaire"))
        return super(Partner, self).write(vals)

Partner()