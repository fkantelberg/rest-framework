Under *Settings > Technical > Database Structure > Serializer* you can configure
the serializers used by your implementation. An additional unique *Code* field is
used to specify which serializer is used by which API method.

The following example requires a serializer with the code ``res.partner`` which is
used for serializing the records returned by the method (exporting mode). If used
as input_param the params will be deserialized and structured in the deserialized
data.

.. code-block:: python

    from odoo.addons.component.core import Component


    class PartnerService(Component):
        _name = "serializer.service"
        _inherit = "base.rest.service"
        _usage = "test"
        _collection = "base.rest.serializer"
        _description = """Returns all partners"""

        @restapi.method(
            [(["/"], "GET")],
            output_param=restapi.Serializer("res.partner", is_list=True),
            auth="public",
        )
        def get(self):
            return self.env["res.partner"].search([])
