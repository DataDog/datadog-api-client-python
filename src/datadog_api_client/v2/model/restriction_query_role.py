# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.restriction_query_role_attribute import RestrictionQueryRoleAttribute
    from datadog_api_client.v2.model.roles_type import RolesType


class RestrictionQueryRole(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.restriction_query_role_attribute import RestrictionQueryRoleAttribute
        from datadog_api_client.v2.model.roles_type import RolesType

        return {
            "attributes": (RestrictionQueryRoleAttribute,),
            "id": (str,),
            "type": (RolesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RestrictionQueryRoleAttribute, id: str, type: RolesType, **kwargs):
        """
        Partial role object.

        :param attributes: Attributes of the role for a restriction query.
        :type attributes: RestrictionQueryRoleAttribute

        :param id: ID of the role.
        :type id: str

        :param type: Roles type.
        :type type: RolesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
