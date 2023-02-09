# © 2023 Florian Kantelberg - initOS GmbH
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Base Rest Serializer",
    "summary": "Glue module to combine the serializer with the rest framework",
    "license": "AGPL-3",
    "version": "16.0.1.0.0",
    "website": "https://github.com/OCA/rest-framework",
    "author": "initOS GmbH, Odoo Community Association (OCA)",
    "depends": ["base_rest", "base_serializer"],
    "data": [
        "security/ir.model.access.csv",
        "views/serializer_views.xml",
        "views/serializer_schema_views.xml",
    ],
    "auto_install": True,
    "installable": True,
}
