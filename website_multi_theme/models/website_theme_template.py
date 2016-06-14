# -*- coding: utf-8 -*-
# © 2016 Antonio Espinosa - <antonio.espinosa@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class WebsiteTheme(models.Model):
    _name = 'website.theme.template'

    name = fields.Char(string="Custom template", required=True)
    standard = fields.Char(string="Standard template", required=True)
    theme_id = fields.Many2one(
        string="Theme", comodel_name='website.theme', required=True)
