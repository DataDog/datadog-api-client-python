# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue_watch_action import IssueWatchAction
    from datadog_api_client.v2.model.issue_watch_condition import IssueWatchCondition
    from datadog_api_client.v2.model.issue_watch_status import IssueWatchStatus


class IssueWatchAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_watch_action import IssueWatchAction
        from datadog_api_client.v2.model.issue_watch_condition import IssueWatchCondition
        from datadog_api_client.v2.model.issue_watch_status import IssueWatchStatus

        return {
            "action": (IssueWatchAction,),
            "condition": (IssueWatchCondition,),
            "started_at": (datetime,),
            "status": (IssueWatchStatus,),
        }

    attribute_map = {
        "action": "action",
        "condition": "condition",
        "started_at": "started_at",
        "status": "status",
    }

    def __init__(
        self_,
        action: Union[IssueWatchAction, UnsetType] = unset,
        condition: Union[IssueWatchCondition, UnsetType] = unset,
        started_at: Union[datetime, UnsetType] = unset,
        status: Union[IssueWatchStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the information of a watch.

        :param action: Action applied to the issue when the watch condition is met.
        :type action: IssueWatchAction, optional

        :param condition: Condition that triggers the watch action. The fields that are set depend on ``kind`` :
            ``OCCURRENCES`` uses ``threshold`` , ``CARDINALITY`` uses ``threshold`` and ``projection`` ,
            ``ELAPSED_TIME`` uses ``duration`` , and ``ANY`` and ``ALL`` use ``operands``.
        :type condition: IssueWatchCondition, optional

        :param started_at: Timestamp of when the watch started.
        :type started_at: datetime, optional

        :param status: Status of the watch.
        :type status: IssueWatchStatus, optional
        """
        if action is not unset:
            kwargs["action"] = action
        if condition is not unset:
            kwargs["condition"] = condition
        if started_at is not unset:
            kwargs["started_at"] = started_at
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
