# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class AuthNMappingAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attribute_key": (str,),
            "attribute_value": (str,),
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "saml_assertion_attribute_id": (str,),
        }

    attribute_map = {
        "attribute_key": "attribute_key",
        "attribute_value": "attribute_value",
        "created_at": "created_at",
        "modified_at": "modified_at",
        "saml_assertion_attribute_id": "saml_assertion_attribute_id",
    }
    read_only_vars = {
        "created_at",
        "modified_at",
    }

    def __init__(self, *args, **kwargs):
        """
        Attributes of AuthN Mapping.

        :param attribute_key: Key portion of a key/value pair of the attribute sent from the Identity Provider.
        :type attribute_key: str, optional

        :param attribute_value: Value portion of a key/value pair of the attribute sent from the Identity Provider.
        :type attribute_value: str, optional

        :param created_at: Creation time of the AuthN Mapping.
        :type created_at: datetime, optional

        :param modified_at: Time of last AuthN Mapping modification.
        :type modified_at: datetime, optional

        :param saml_assertion_attribute_id: The ID of the SAML assertion attribute.
        :type saml_assertion_attribute_id: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuthNMappingAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
