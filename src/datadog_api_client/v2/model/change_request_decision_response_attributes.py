# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.change_request_decision_status_type import ChangeRequestDecisionStatusType


class ChangeRequestDecisionResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_decision_status_type import ChangeRequestDecisionStatusType

        return {
            "change_request_status": (ChangeRequestDecisionStatusType,),
            "decided_at": (datetime,),
            "decision_reason": (str,),
            "deleted_at": (datetime,),
            "request_reason": (str,),
            "requested_at": (datetime,),
        }

    attribute_map = {
        "change_request_status": "change_request_status",
        "decided_at": "decided_at",
        "decision_reason": "decision_reason",
        "deleted_at": "deleted_at",
        "request_reason": "request_reason",
        "requested_at": "requested_at",
    }

    def __init__(
        self_,
        change_request_status: ChangeRequestDecisionStatusType,
        decided_at: datetime,
        decision_reason: str,
        deleted_at: datetime,
        request_reason: str,
        requested_at: datetime,
        **kwargs,
    ):
        """
        Attributes of a change request decision in a response.

        :param change_request_status: The status of a change request decision.
        :type change_request_status: ChangeRequestDecisionStatusType

        :param decided_at: Timestamp of when the decision was made.
        :type decided_at: datetime

        :param decision_reason: The reason for the decision.
        :type decision_reason: str

        :param deleted_at: Timestamp of when the decision was deleted.
        :type deleted_at: datetime

        :param request_reason: The reason for requesting the decision.
        :type request_reason: str

        :param requested_at: Timestamp of when the decision was requested.
        :type requested_at: datetime
        """
        super().__init__(kwargs)

        self_.change_request_status = change_request_status
        self_.decided_at = decided_at
        self_.decision_reason = decision_reason
        self_.deleted_at = deleted_at
        self_.request_reason = request_reason
        self_.requested_at = requested_at
