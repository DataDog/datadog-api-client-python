# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.nullable_user_relationship import NullableUserRelationship


class AutomationRuleRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nullable_user_relationship import NullableUserRelationship

        return {
            "created_by": (NullableUserRelationship,),
            "modified_by": (NullableUserRelationship,),
        }

    attribute_map = {
        "created_by": "created_by",
        "modified_by": "modified_by",
    }

    def __init__(
        self_,
        created_by: Union[NullableUserRelationship, none_type, UnsetType] = unset,
        modified_by: Union[NullableUserRelationship, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Related resources for the automation rule, including the users who created and last modified it.

        :param created_by: Relationship to user.
        :type created_by: NullableUserRelationship, none_type, optional

        :param modified_by: Relationship to user.
        :type modified_by: NullableUserRelationship, none_type, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if modified_by is not unset:
            kwargs["modified_by"] = modified_by
        super().__init__(kwargs)
