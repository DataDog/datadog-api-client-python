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
    from datadog_api_client.v2.model.get_data_observability_monitor_run_status_response_data import (
        GetDataObservabilityMonitorRunStatusResponseData,
    )


class GetDataObservabilityMonitorRunStatusResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_data_observability_monitor_run_status_response_data import (
            GetDataObservabilityMonitorRunStatusResponseData,
        )

        return {
            "data": (GetDataObservabilityMonitorRunStatusResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GetDataObservabilityMonitorRunStatusResponseData, **kwargs):
        """
        The response for getting the status of a data observability monitor run.

        :param data: The data object for a data observability monitor run status response.
        :type data: GetDataObservabilityMonitorRunStatusResponseData
        """
        super().__init__(kwargs)

        self_.data = data
