# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuthNMappingRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
        from datadog_api_client.v2.model.relationship_to_saml_assertion_attribute import (
            RelationshipToSAMLAssertionAttribute,
        )

        return {
            "role": (RelationshipToRole,),
            "saml_assertion_attribute": (RelationshipToSAMLAssertionAttribute,),
        }

    attribute_map = {
        "role": "role",
        "saml_assertion_attribute": "saml_assertion_attribute",
    }

    def __init__(self, *args, **kwargs):
        """
        All relationships associated with AuthN Mapping.

        :param role: Relationship to role.
        :type role: RelationshipToRole, optional

        :param saml_assertion_attribute: AuthN Mapping relationship to SAML Assertion Attribute.
        :type saml_assertion_attribute: RelationshipToSAMLAssertionAttribute, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuthNMappingRelationships, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
