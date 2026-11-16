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
    from datadog_api_client.v2.model.issue_watch_condition import IssueWatchCondition


class IssueSnoozeRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_watch_condition import IssueWatchCondition

        return {
            "condition": (IssueWatchCondition,),
        }

    attribute_map = {
        "condition": "condition",
    }

    def __init__(self_, condition: IssueWatchCondition, **kwargs):
        """
        Object describing an issue snooze request.

        :param condition: Condition that triggers the watch action. The fields that are set depend on ``kind`` :
            ``OCCURRENCES`` uses ``threshold`` , ``CARDINALITY`` uses ``threshold`` and ``projection`` ,
            ``ELAPSED_TIME`` uses ``duration`` , and ``ANY`` and ``ALL`` use ``operands``.
        :type condition: IssueWatchCondition
        """
        super().__init__(kwargs)

        self_.condition = condition
