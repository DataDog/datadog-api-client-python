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
    from datadog_api_client.v2.model.data_observability_monitor_run_status import DataObservabilityMonitorRunStatus


class GetDataObservabilityMonitorRunStatusResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.data_observability_monitor_run_status import DataObservabilityMonitorRunStatus

        return {
            "error_message": (str,),
            "status": (DataObservabilityMonitorRunStatus,),
        }

    attribute_map = {
        "error_message": "error_message",
        "status": "status",
    }

    def __init__(
        self_, status: DataObservabilityMonitorRunStatus, error_message: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        The attributes of a data observability monitor run status response.

        :param error_message: Error message describing why the monitor run failed. Only present when status is error.
        :type error_message: str, optional

        :param status: The status of a data observability monitor run.
        :type status: DataObservabilityMonitorRunStatus
        """
        if error_message is not unset:
            kwargs["error_message"] = error_message
        super().__init__(kwargs)

        self_.status = status
