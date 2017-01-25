# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError,ValidationError




class Partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, data):
        user = self.env['res.users'].browse(self.env.uid)
        if not user.has_group('partner_wkf.partner_group_user'):
             raise UserError(_("Vous n'avez pas le droit de créer un partenaire"))
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