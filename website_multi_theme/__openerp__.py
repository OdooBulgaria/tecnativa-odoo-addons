# -*- coding: utf-8 -*-
# © 2016 Antonio Espinosa - <antonio.espinosa@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Website multi theme",
    "summary": "Support for multiple themes",
    "version": "8.0.1.0.0",
    "category": "Website",
    "website": "http://www.tecnativa.com",
    "author": "Tecnativa",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    # 'auto_install':False,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "website_multi",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/website_view.xml",
        "views/website_templates.xml",
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
