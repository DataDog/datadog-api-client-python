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


class ChangeRequestDecisionUpdateDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_decisions_relationship import ChangeRequestDecisionsRelationship

        return {
            "change_request_decisions": (ChangeRequestDecisionsRelationship,),
        }

    attribute_map = {
        "change_request_decisions": "change_request_decisions",
    }

    def __init__(self_, change_request_decisions: ChangeRequestDecisionsRelationship, **kwargs):
        """
        Relationships for updating a change request decision.

        :param change_request_decisions: Relationship to change request decisions.
        :type change_request_decisions: ChangeRequestDecisionsRelationship
        """
        super().__init__(kwargs)

        self_.change_request_decisions = change_request_decisions
