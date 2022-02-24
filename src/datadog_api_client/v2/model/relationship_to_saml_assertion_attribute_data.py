# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.saml_assertion_attributes_type import SAMLAssertionAttributesType

    globals()["SAMLAssertionAttributesType"] = SAMLAssertionAttributesType


class RelationshipToSAMLAssertionAttributeData(ModelNormal):

    validations = {
        "id": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "id": (int,),
            "type": (SAMLAssertionAttributesType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, id, type, *args, **kwargs):
        """
        Data of AuthN Mapping relationship to SAML Assertion Attribute.

        :param id: The ID of the SAML assertion attribute.
        :type id: int

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

        self = super(RelationshipToSAMLAssertionAttributeData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
