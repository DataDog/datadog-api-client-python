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
    from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser


class IncidentImportRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser

        return {
            "commander_user": (NullableRelationshipToUser,),
            "declared_by_user": (NullableRelationshipToUser,),
        }

    attribute_map = {
        "commander_user": "commander_user",
        "declared_by_user": "declared_by_user",
    }

    def __init__(
        self_,
        commander_user: Union[NullableRelationshipToUser, none_type, UnsetType] = unset,
        declared_by_user: Union[NullableRelationshipToUser, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The relationships for an incident import request.

        :param commander_user: Relationship to user.
        :type commander_user: NullableRelationshipToUser, none_type, optional

        :param declared_by_user: Relationship to user.
        :type declared_by_user: NullableRelationshipToUser, none_type, optional
        """
        if commander_user is not unset:
            kwargs["commander_user"] = commander_user
        if declared_by_user is not unset:
            kwargs["declared_by_user"] = declared_by_user
        super().__init__(kwargs)
