# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue_watch_condition_kind import IssueWatchConditionKind


class IssueWatchCondition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_watch_condition_kind import IssueWatchConditionKind

        return {
            "duration": (str,),
            "kind": (IssueWatchConditionKind,),
            "operands": ([IssueWatchCondition],),
            "projection": ([str],),
            "threshold": (int,),
        }

    attribute_map = {
        "duration": "duration",
        "kind": "kind",
        "operands": "operands",
        "projection": "projection",
        "threshold": "threshold",
    }

    def __init__(
        self_,
        kind: IssueWatchConditionKind,
        duration: Union[str, UnsetType] = unset,
        operands: Union[List[IssueWatchCondition], UnsetType] = unset,
        projection: Union[List[str], UnsetType] = unset,
        threshold: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Condition that triggers the watch action. The fields that are set depend on ``kind`` :
        ``OCCURRENCES`` uses ``threshold`` , ``CARDINALITY`` uses ``threshold`` and ``projection`` ,
        ``ELAPSED_TIME`` uses ``duration`` , and ``ANY`` and ``ALL`` use ``operands``.

        :param duration: Time that must elapse before the condition is met, as a Go duration string.
        :type duration: str, optional

        :param kind: Kind of watch condition.
        :type kind: IssueWatchConditionKind

        :param operands: Nested conditions combined by ``ANY`` or ``ALL``.
        :type operands: [IssueWatchCondition], optional

        :param projection: Attributes whose distinct values are counted for ``CARDINALITY``.
        :type projection: [str], optional

        :param threshold: Number of occurrences, or of distinct values for ``CARDINALITY`` , that triggers the condition.
        :type threshold: int, optional
        """
        if duration is not unset:
            kwargs["duration"] = duration
        if operands is not unset:
            kwargs["operands"] = operands
        if projection is not unset:
            kwargs["projection"] = projection
        if threshold is not unset:
            kwargs["threshold"] = threshold
        super().__init__(kwargs)

        self_.kind = kind
