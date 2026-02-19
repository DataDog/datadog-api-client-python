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
    from datadog_api_client.v2.model.change_request_user_relationship import ChangeRequestUserRelationship


class ChangeRequestDecisionRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_user_relationship import ChangeRequestUserRelationship

        return {
            "modified_by": (ChangeRequestUserRelationship,),
            "requested_by_user": (ChangeRequestUserRelationship,),
            "requested_user": (ChangeRequestUserRelationship,),
        }

    attribute_map = {
        "modified_by": "modified_by",
        "requested_by_user": "requested_by_user",
        "requested_user": "requested_user",
    }

    def __init__(
        self_,
        modified_by: ChangeRequestUserRelationship,
        requested_by_user: ChangeRequestUserRelationship,
        requested_user: ChangeRequestUserRelationship,
        **kwargs,
    ):
        """
        Relationships of a change request decision.

        :param modified_by: Relationship to a user.
        :type modified_by: ChangeRequestUserRelationship

        :param requested_by_user: Relationship to a user.
        :type requested_by_user: ChangeRequestUserRelationship

        :param requested_user: Relationship to a user.
        :type requested_user: ChangeRequestUserRelationship
        """
        super().__init__(kwargs)

        self_.modified_by = modified_by
        self_.requested_by_user = requested_by_user
        self_.requested_user = requested_user
