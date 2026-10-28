# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.data_observability_monitor_run_group import DataObservabilityMonitorRunGroup
    from datadog_api_client.v2.model.data_observability_monitor_run_status import DataObservabilityMonitorRunStatus


class GetDataObservabilityMonitorRunStatusResponseAttributes(ModelNormal):
    validations = {
        "groups": {
            "max_items": 1000,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.data_observability_monitor_run_group import DataObservabilityMonitorRunGroup
        from datadog_api_client.v2.model.data_observability_monitor_run_status import DataObservabilityMonitorRunStatus

        return {
            "error_message": (str,),
            "group_counts": ({str: (int,)},),
            "groups": ([DataObservabilityMonitorRunGroup],),
            "status": (DataObservabilityMonitorRunStatus,),
        }

    attribute_map = {
        "error_message": "error_message",
        "group_counts": "group_counts",
        "groups": "groups",
        "status": "status",
    }

    def __init__(
        self_,
        status: DataObservabilityMonitorRunStatus,
        error_message: Union[str, UnsetType] = unset,
        group_counts: Union[Dict[str, int], UnsetType] = unset,
        groups: Union[List[DataObservabilityMonitorRunGroup], UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a data observability monitor run status response.

        :param error_message: Error message describing why the monitor run failed. Only present when status is error.
        :type error_message: str, optional

        :param group_counts: The number of the monitor's groups in each state, once the run has finished.
        :type group_counts: {str: (int,)}, optional

        :param groups: The first 1,000 of the monitor's groups that are not ok, once the run has finished. List the monitor's groups for all of them.
        :type groups: [DataObservabilityMonitorRunGroup], optional

        :param status: The status of a data observability monitor run.
        :type status: DataObservabilityMonitorRunStatus
        """
        if error_message is not unset:
            kwargs["error_message"] = error_message
        if group_counts is not unset:
            kwargs["group_counts"] = group_counts
        if groups is not unset:
            kwargs["groups"] = groups
        super().__init__(kwargs)

        self_.status = status
