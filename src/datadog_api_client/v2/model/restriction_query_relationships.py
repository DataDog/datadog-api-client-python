# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles


class RestrictionQueryRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles

        return {
            "roles": (RelationshipToRoles,),
        }

    attribute_map = {
        "roles": "roles",
    }

    def __init__(self_, roles: Union[RelationshipToRoles, UnsetType] = unset, **kwargs):
        """
        Relationships of the restriction query object.

        :param roles: Relationship to roles.
        :type roles: RelationshipToRoles, optional
        """
        if roles is not unset:
            kwargs["roles"] = roles
        super().__init__(kwargs)
