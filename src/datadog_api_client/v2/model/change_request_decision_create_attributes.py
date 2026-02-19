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
    from datadog_api_client.v2.model.change_request_decision_status_type import ChangeRequestDecisionStatusType


class ChangeRequestDecisionCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_decision_status_type import ChangeRequestDecisionStatusType

        return {
            "change_request_status": (ChangeRequestDecisionStatusType,),
            "request_reason": (str,),
        }

    attribute_map = {
        "change_request_status": "change_request_status",
        "request_reason": "request_reason",
    }

    def __init__(
        self_,
        change_request_status: Union[ChangeRequestDecisionStatusType, UnsetType] = unset,
        request_reason: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a change request decision.

        :param change_request_status: The status of a change request decision.
        :type change_request_status: ChangeRequestDecisionStatusType, optional

        :param request_reason: The reason for requesting the decision.
        :type request_reason: str, optional
        """
        if change_request_status is not unset:
            kwargs["change_request_status"] = change_request_status
        if request_reason is not unset:
            kwargs["request_reason"] = request_reason
        super().__init__(kwargs)
