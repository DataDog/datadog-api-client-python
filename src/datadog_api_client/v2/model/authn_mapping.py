# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuthNMapping(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.authn_mapping_attributes import AuthNMappingAttributes
        from datadog_api_client.v2.model.authn_mapping_relationships import AuthNMappingRelationships
        from datadog_api_client.v2.model.authn_mappings_type import AuthNMappingsType

        return {
            "attributes": (AuthNMappingAttributes,),
            "id": (str,),
            "relationships": (AuthNMappingRelationships,),
            "type": (AuthNMappingsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self, id, type, *args, **kwargs):
        """
        The AuthN Mapping object returned by API.

        :param attributes: Attributes of AuthN Mapping.
        :type attributes: AuthNMappingAttributes, optional

        :param id: ID of the AuthN Mapping.
        :type id: str

        :param relationships: All relationships associated with AuthN Mapping.
        :type relationships: AuthNMappingRelationships, optional

        :param type: AuthN Mappings resource type.
        :type type: AuthNMappingsType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuthNMapping, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
