# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.auth_n_mapping_create_attributes import AuthNMappingCreateAttributes
    from datadog_api_client.v2.model.auth_n_mapping_create_relationships import AuthNMappingCreateRelationships
    from datadog_api_client.v2.model.auth_n_mappings_type import AuthNMappingsType

    globals()["AuthNMappingCreateAttributes"] = AuthNMappingCreateAttributes
    globals()["AuthNMappingCreateRelationships"] = AuthNMappingCreateRelationships
    globals()["AuthNMappingsType"] = AuthNMappingsType


class AuthNMappingCreateData(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (AuthNMappingCreateAttributes,),
            "relationships": (AuthNMappingCreateRelationships,),
            "type": (AuthNMappingsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, type, *args, **kwargs):
        """
        Data for creating an AuthN Mapping.

        :param attributes: Key/Value pair of attributes used for create request.
        :type attributes: AuthNMappingCreateAttributes, optional

        :param relationships: Relationship of AuthN Mapping create object to Role.
        :type relationships: AuthNMappingCreateRelationships, optional

        :param type: AuthN Mappings resource type.
        :type type: AuthNMappingsType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuthNMappingCreateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
