# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SAMLAssertionAttribute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saml_assertion_attribute_attributes import SAMLAssertionAttributeAttributes
        from datadog_api_client.v2.model.saml_assertion_attributes_type import SAMLAssertionAttributesType

        return {
            "attributes": (SAMLAssertionAttributeAttributes,),
            "id": (str,),
            "type": (SAMLAssertionAttributesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, id, type, *args, **kwargs):
        """
        SAML assertion attribute.

        :param attributes: Key/Value pair of attributes used in SAML assertion attributes.
        :type attributes: SAMLAssertionAttributeAttributes, optional

        :param id: The ID of the SAML assertion attribute.
        :type id: str

        :param type: SAML assertion attributes resource type.
        :type type: SAMLAssertionAttributesType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SAMLAssertionAttribute, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
