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
    from datadog_api_client.v2.model.synthetics_test_options_monitor_options import SyntheticsTestOptionsMonitorOptions
    from datadog_api_client.v2.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
    from datadog_api_client.v2.model.synthetics_test_options_scheduling import SyntheticsTestOptionsScheduling


class SyntheticsTestOptions(ModelNormal):
    validations = {
        "monitor_priority": {
            "inclusive_maximum": 5,
            "inclusive_minimum": 1,
        },
        "tick_every": {
            "inclusive_maximum": 604800,
            "inclusive_minimum": 30,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_options_monitor_options import (
            SyntheticsTestOptionsMonitorOptions,
        )
        from datadog_api_client.v2.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
        from datadog_api_client.v2.model.synthetics_test_options_scheduling import SyntheticsTestOptionsScheduling

        return {
            "min_failure_duration": (int,),
            "min_location_failed": (int,),
            "monitor_name": (str,),
            "monitor_options": (SyntheticsTestOptionsMonitorOptions,),
            "monitor_priority": (int,),
            "restricted_roles": ([str],),
            "retry": (SyntheticsTestOptionsRetry,),
            "scheduling": (SyntheticsTestOptionsScheduling,),
            "tick_every": (int,),
        }

    attribute_map = {
        "min_failure_duration": "min_failure_duration",
        "min_location_failed": "min_location_failed",
        "monitor_name": "monitor_name",
        "monitor_options": "monitor_options",
        "monitor_priority": "monitor_priority",
        "restricted_roles": "restricted_roles",
        "retry": "retry",
        "scheduling": "scheduling",
        "tick_every": "tick_every",
    }

    def __init__(
        self_,
        min_failure_duration: Union[int, UnsetType] = unset,
        min_location_failed: Union[int, UnsetType] = unset,
        monitor_name: Union[str, UnsetType] = unset,
        monitor_options: Union[SyntheticsTestOptionsMonitorOptions, UnsetType] = unset,
        monitor_priority: Union[int, UnsetType] = unset,
        restricted_roles: Union[List[str], UnsetType] = unset,
        retry: Union[SyntheticsTestOptionsRetry, UnsetType] = unset,
        scheduling: Union[SyntheticsTestOptionsScheduling, UnsetType] = unset,
        tick_every: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing the extra options for a Synthetic test.

        :param min_failure_duration: Minimum amount of time in failure required to trigger an alert.
        :type min_failure_duration: int, optional

        :param min_location_failed: Minimum number of locations in failure required to trigger
            an alert.
        :type min_location_failed: int, optional

        :param monitor_name: The monitor name is used for the alert title as well as for all monitor dashboard widgets and SLOs.
        :type monitor_name: str, optional

        :param monitor_options: Object containing the options for a Synthetic test as a monitor
            (for example, renotification).
        :type monitor_options: SyntheticsTestOptionsMonitorOptions, optional

        :param monitor_priority: Integer from 1 (high) to 5 (low) indicating alert severity.
        :type monitor_priority: int, optional

        :param restricted_roles: A list of role identifiers that can be pulled from the Roles API, for restricting read and write access. This field is deprecated. Use the restriction policies API to manage permissions. **Deprecated**.
        :type restricted_roles: [str], optional

        :param retry: Object describing the retry strategy to apply to a Synthetic test.
        :type retry: SyntheticsTestOptionsRetry, optional

        :param scheduling: Object containing timeframes and timezone used for advanced scheduling.
        :type scheduling: SyntheticsTestOptionsScheduling, optional

        :param tick_every: The frequency at which to run the Synthetic test (in seconds).
        :type tick_every: int, optional
        """
        if min_failure_duration is not unset:
            kwargs["min_failure_duration"] = min_failure_duration
        if min_location_failed is not unset:
            kwargs["min_location_failed"] = min_location_failed
        if monitor_name is not unset:
            kwargs["monitor_name"] = monitor_name
        if monitor_options is not unset:
            kwargs["monitor_options"] = monitor_options
        if monitor_priority is not unset:
            kwargs["monitor_priority"] = monitor_priority
        if restricted_roles is not unset:
            kwargs["restricted_roles"] = restricted_roles
        if retry is not unset:
            kwargs["retry"] = retry
        if scheduling is not unset:
            kwargs["scheduling"] = scheduling
        if tick_every is not unset:
            kwargs["tick_every"] = tick_every
        super().__init__(kwargs)
