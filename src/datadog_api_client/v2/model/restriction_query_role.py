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
    from datadog_api_client.v2.model.restriction_query_role_attribute import RestrictionQueryRoleAttribute


class RestrictionQueryRole(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.restriction_query_role_attribute import RestrictionQueryRoleAttribute

        return {
            "attributes": (RestrictionQueryRoleAttribute,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "type",
    }

    def __init__(
        self_,
        attributes: Union[RestrictionQueryRoleAttribute, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Partial role object.

        :param attributes: Attributes of the role for a restriction query.
        :type attributes: RestrictionQueryRoleAttribute, optional

        :param id: ID of the role.
        :type id: str, optional

        :param type: Role resource type.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
