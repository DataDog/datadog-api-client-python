# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuthNMappingUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.authn_mapping_update_attributes import AuthNMappingUpdateAttributes
        from datadog_api_client.v2.model.authn_mapping_update_relationships import AuthNMappingUpdateRelationships
        from datadog_api_client.v2.model.authn_mappings_type import AuthNMappingsType

        return {
            "attributes": (AuthNMappingUpdateAttributes,),
            "id": (str,),
            "relationships": (AuthNMappingUpdateRelationships,),
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
        Data for updating an AuthN Mapping.

        :param attributes: Key/Value pair of attributes used for update request.
        :type attributes: AuthNMappingUpdateAttributes, optional

        :param id: ID of the AuthN Mapping.
        :type id: str

        :param relationships: Relationship of AuthN Mapping update object to Role.
        :type relationships: AuthNMappingUpdateRelationships, optional

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

        self = super(AuthNMappingUpdateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
