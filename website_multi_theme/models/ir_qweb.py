# -*- coding: utf-8 -*-
# © 2016 Antonio Espinosa - <antonio.espinosa@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class IrQweb(models.Model):
    _inherit = "ir.qweb"

    def render_tag_call(self, element, template_attributes,
                        generated_attributes, qwebcontext):
        _logger.info('render_tag_call: element = %s', element)
        _logger.info('render_tag_call: template_attributes = %s', template_attributes)
        return super(IrQweb, self).render_tag_call(
            element, template_attributes, generated_attributes, qwebcontext)
