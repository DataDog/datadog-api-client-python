# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class AuthNMappingIncluded(ModelComposed):
    def __init__(self, *args, **kwargs):
        """
        Included data in the AuthN Mapping response.

        :param attributes: Key/Value pair of attributes used in SAML assertion attributes.
        :type attributes: SAMLAssertionAttributeAttributes, optional

        :param id: The ID of the SAML assertion attribute.
        :type id: str

        :param type: SAML assertion attributes resource type.
        :type type: SAMLAssertionAttributesType

        :param relationships: Relationships of the role object returned by the API.
        :type relationships: RoleResponseRelationships, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuthNMappingIncluded, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.saml_assertion_attribute import SAMLAssertionAttribute
        from datadog_api_client.v2.model.role import Role

        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [
                SAMLAssertionAttribute,
                Role,
            ],
        }
