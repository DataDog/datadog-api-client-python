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
    from datadog_api_client.v2.model.change_request_decisions_relationship import ChangeRequestDecisionsRelationship
    from datadog_api_client.v2.model.change_request_user_relationship import ChangeRequestUserRelationship


class ChangeRequestRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_decisions_relationship import ChangeRequestDecisionsRelationship
        from datadog_api_client.v2.model.change_request_user_relationship import ChangeRequestUserRelationship

        return {
            "change_request_decisions": (ChangeRequestDecisionsRelationship,),
            "created_by": (ChangeRequestUserRelationship,),
            "modified_by": (ChangeRequestUserRelationship,),
        }

    attribute_map = {
        "change_request_decisions": "change_request_decisions",
        "created_by": "created_by",
        "modified_by": "modified_by",
    }

    def __init__(
        self_,
        change_request_decisions: ChangeRequestDecisionsRelationship,
        created_by: ChangeRequestUserRelationship,
        modified_by: ChangeRequestUserRelationship,
        **kwargs,
    ):
        """
        Relationships of a change request.

        :param change_request_decisions: Relationship to change request decisions.
        :type change_request_decisions: ChangeRequestDecisionsRelationship

        :param created_by: Relationship to a user.
        :type created_by: ChangeRequestUserRelationship

        :param modified_by: Relationship to a user.
        :type modified_by: ChangeRequestUserRelationship
        """
        super().__init__(kwargs)

        self_.change_request_decisions = change_request_decisions
        self_.created_by = created_by
        self_.modified_by = modified_by
