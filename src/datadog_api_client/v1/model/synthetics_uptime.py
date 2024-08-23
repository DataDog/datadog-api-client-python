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
    from datadog_api_client.v1.model.slo_history_response_error_with_type import SLOHistoryResponseErrorWithType


class SyntheticsUptime(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_history_response_error_with_type import SLOHistoryResponseErrorWithType

        return {
            "errors": ([SLOHistoryResponseErrorWithType],),
            "group": (str,),
            "history": ([[float]],),
            "span_precision": (float,),
            "uptime": (float,),
        }

    attribute_map = {
        "errors": "errors",
        "group": "group",
        "history": "history",
        "span_precision": "span_precision",
        "uptime": "uptime",
    }

    def __init__(
        self_,
        errors: Union[List[SLOHistoryResponseErrorWithType], UnsetType] = unset,
        group: Union[str, UnsetType] = unset,
        history: Union[List[List[float]], UnsetType] = unset,
        span_precision: Union[float, UnsetType] = unset,
        uptime: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the uptime information.

        :param errors: An array of error objects returned while querying the history data for the service level objective.
        :type errors: [SLOHistoryResponseErrorWithType], optional

        :param group: For groups in a grouped SLO, this is the group name.
        :type group: str, optional

        :param history: The state transition history for the monitor. It is represented as
            an array of pairs. Each pair is an array containing the timestamp of the transition
            as an integer in Unix epoch format in the first element, and the state as an integer in the
            second element. An integer value of ``0`` for state means uptime, ``1`` means downtime, and ``2`` means no data.
        :type history: [[float]], optional

        :param span_precision: The amount of decimal places the SLI value is accurate to for the given from ``&&`` to timestamp.
        :type span_precision: float, optional

        :param uptime: The overall uptime.
        :type uptime: float, optional
        """
        if errors is not unset:
            kwargs["errors"] = errors
        if group is not unset:
            kwargs["group"] = group
        if history is not unset:
            kwargs["history"] = history
        if span_precision is not unset:
            kwargs["span_precision"] = span_precision
        if uptime is not unset:
            kwargs["uptime"] = uptime
        super().__init__(kwargs)
