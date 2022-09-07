# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuthNMappingCreateRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole

        return {
            "role": (RelationshipToRole,),
        }

    attribute_map = {
        "role": "role",
    }

    def __init__(self_, *args, **kwargs):
        """
        Relationship of AuthN Mapping create object to Role.

        :param role: Relationship to role.
        :type role: RelationshipToRole, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
