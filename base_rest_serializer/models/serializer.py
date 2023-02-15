# © 2023 Florian Kantelberg - initOS GmbH
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class Serializer(models.Model):
    _inherit = "ir.serializer"

    code = fields.Char(help="Unique code for this serializer referred by the API")
    schema_ids = fields.One2many("ir.serializer.schema", "serializer_id")

    @api.constrains("code")
    def _check_code(self):
        for rec in self.filtered("code"):
            if self.search_count([("code", "=", rec.code)]) > 1:
                raise ValidationError(_("Code must be unique"))

    def find_by_code(self, code):
        return self.search([("code", "=", code)])

    def api_reference(self):
        self.ensure_one()
        return f"{self.name}"

    def to_schema(self, direction):
        self.ensure_one()

        # Call the schema generation on the basis
        if self.base_serializer_id:
            result = self.base_serializer_id.to_schema(direction)
            required = set(result.get("required") or [])
            props = result.get("properties", {})
        else:
            required = set()
            props = {}

        dir_domain = [(direction, "=", True)]
        schemes = self.schema_ids.filtered_domain(dir_domain)
        required.update(schemes.filtered("required").mapped("name"))

        fields = self.field_ids.filtered_domain(dir_domain)
        props.update(fields.to_schema())

        required.update(
            field.name or field.field_id.name
            for field in fields
            if field.required or field.field_id.required
        )

        props.update(schemes.to_schema())

        return {"type": "object", "required": sorted(required), "properties": props}
