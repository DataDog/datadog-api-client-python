# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
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
            "errors": ([SLOHistoryResponseErrorWithType], none_type),
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
        errors: Union[List[SLOHistoryResponseErrorWithType], none_type, UnsetType] = unset,
        group: Union[str, UnsetType] = unset,
        history: Union[List[List[float]], UnsetType] = unset,
        span_precision: Union[float, UnsetType] = unset,
        uptime: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the uptime information.

        :param errors: An array of error objects returned while querying the history data for the service level objective.
        :type errors: [SLOHistoryResponseErrorWithType], none_type, optional

        :param group: The location name
        :type group: str, optional

        :param history: The state transition history for the monitor, represented as an array of
            pairs. Each pair is an array where the first element is the transition timestamp
            in Unix epoch format (integer) and the second element is the state (integer).
            For the state, an integer value of ``0`` indicates uptime, ``1`` indicates downtime,
            and ``2`` indicates no data.
        :type history: [[float]], optional

        :param span_precision: The number of decimal places to which the SLI value is accurate for the given from-to timestamps.
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
