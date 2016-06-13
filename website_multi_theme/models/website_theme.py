# -*- coding: utf-8 -*-
# © 2016 Antonio Espinosa - <antonio.espinosa@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class WebsiteTheme(models.Model):
    _name = 'website.theme'

    name = fields.Char(required=True)
    css_class = fields.Char(string='CSS class', required=True)
