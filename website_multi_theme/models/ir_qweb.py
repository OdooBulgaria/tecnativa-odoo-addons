# -*- coding: utf-8 -*-
# © 2016 Antonio Espinosa - <antonio.espinosa@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models
import logging
_logger = logging.getLogger(__name__)


class IrQweb(models.Model):
    _inherit = "ir.qweb"

    def render_tag_call(self, element, template_attributes,
                        generated_attributes, qwebcontext):
        _logger.info('render_tag_call: element = %s', element)
        _logger.info('render_tag_call: template_attributes = %s', template_attributes)
        ctx = qwebcontext.copy()
        cr = ctx.get('request') and ctx['request'].cr or None
        uid = ctx.get('request') and ctx['request'].uid or None
        template = template_attributes.get("call")
        website = self.pool['website'].get_current_website(
            cr, uid, context=ctx)
        if template and website.theme_id:
            custom = self.pool['website.theme.template'].search(cr, uid, [
                ('standard', '=', template),
                ('theme_id', '=', website.theme_id.id),
            ], context=ctx)
            if custom:
                _logger.info('render_tag_call: %s -> %s', template_attributes['call'], custom.name)
                template_attributes['call'] = custom.name
        return super(IrQweb, self).render_tag_call(
            element, template_attributes, generated_attributes, qwebcontext)
