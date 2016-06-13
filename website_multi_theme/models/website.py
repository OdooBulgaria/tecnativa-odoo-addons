# -*- coding: utf-8 -*-
# © 2016 Antonio Espinosa - <antonio.espinosa@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class Website(models.Model):
    _inherit = "website"

    theme_id = fields.Many2one(string="Theme", comodel_name='website.theme')
    css_class = fields.Char(
        string="CSS class", readonly=True, related="theme_id.css_class")
