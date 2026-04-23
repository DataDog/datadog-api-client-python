# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_duration import SyntheticsTestResultDuration


class SyntheticsTestResultExecutionInfo(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_duration import SyntheticsTestResultDuration

        return {
            "duration": (SyntheticsTestResultDuration,),
            "error_message": (str,),
            "is_fast_retry": (bool,),
            "timings": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "tunnel": (bool,),
            "unhealthy": (bool,),
        }

    attribute_map = {
        "duration": "duration",
        "error_message": "error_message",
        "is_fast_retry": "is_fast_retry",
        "timings": "timings",
        "tunnel": "tunnel",
        "unhealthy": "unhealthy",
    }

    def __init__(
        self_,
        duration: Union[SyntheticsTestResultDuration, UnsetType] = unset,
        error_message: Union[str, UnsetType] = unset,
        is_fast_retry: Union[bool, UnsetType] = unset,
        timings: Union[Dict[str, Any], UnsetType] = unset,
        tunnel: Union[bool, UnsetType] = unset,
        unhealthy: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Execution details for a Synthetic test result.

        :param duration: Total duration of a Synthetic test execution.
        :type duration: SyntheticsTestResultDuration, optional

        :param error_message: Error message if the execution encountered an issue.
        :type error_message: str, optional

        :param is_fast_retry: Whether this result is from a fast retry.
        :type is_fast_retry: bool, optional

        :param timings: Timing breakdown of the test execution in milliseconds.
        :type timings: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param tunnel: Whether the test was executed through a tunnel.
        :type tunnel: bool, optional

        :param unhealthy: Whether the location was unhealthy during execution.
        :type unhealthy: bool, optional
        """
        if duration is not unset:
            kwargs["duration"] = duration
        if error_message is not unset:
            kwargs["error_message"] = error_message
        if is_fast_retry is not unset:
            kwargs["is_fast_retry"] = is_fast_retry
        if timings is not unset:
            kwargs["timings"] = timings
        if tunnel is not unset:
            kwargs["tunnel"] = tunnel
        if unhealthy is not unset:
            kwargs["unhealthy"] = unhealthy
        super().__init__(kwargs)
