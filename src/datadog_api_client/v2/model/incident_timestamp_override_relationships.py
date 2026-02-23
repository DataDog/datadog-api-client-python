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
    from datadog_api_client.v2.model.timestamp_override_user_relationship import TimestampOverrideUserRelationship


class IncidentTimestampOverrideRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timestamp_override_user_relationship import TimestampOverrideUserRelationship

        return {
            "created_by_user": (TimestampOverrideUserRelationship,),
            "last_modified_by_user": (TimestampOverrideUserRelationship,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "last_modified_by_user": "last_modified_by_user",
    }

    def __init__(
        self_,
        created_by_user: TimestampOverrideUserRelationship,
        last_modified_by_user: TimestampOverrideUserRelationship,
        **kwargs,
    ):
        """
        Relationships for incident timestamp override.

        :param created_by_user: Relationship to a user.
        :type created_by_user: TimestampOverrideUserRelationship

        :param last_modified_by_user: Relationship to a user.
        :type last_modified_by_user: TimestampOverrideUserRelationship
        """
        super().__init__(kwargs)

        self_.created_by_user = created_by_user
        self_.last_modified_by_user = last_modified_by_user
