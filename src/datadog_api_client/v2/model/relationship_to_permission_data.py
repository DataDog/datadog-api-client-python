# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RelationshipToPermissionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.permissions_type import PermissionsType

        return {
            "id": (str,),
            "type": (PermissionsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, *args, **kwargs):
        """
        Relationship to permission object.

        :param id: ID of the permission.
        :type id: str, optional

        :param type: Permissions resource type.
        :type type: PermissionsType, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
