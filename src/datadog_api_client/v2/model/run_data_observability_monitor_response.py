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
    from datadog_api_client.v2.model.run_data_observability_monitor_response_data import (
        RunDataObservabilityMonitorResponseData,
    )


class RunDataObservabilityMonitorResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.run_data_observability_monitor_response_data import (
            RunDataObservabilityMonitorResponseData,
        )

        return {
            "data": (RunDataObservabilityMonitorResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RunDataObservabilityMonitorResponseData, **kwargs):
        """
        The response returned when a data observability monitor run is triggered.

        :param data: The data object returned when a data observability monitor run is triggered.
        :type data: RunDataObservabilityMonitorResponseData
        """
        super().__init__(kwargs)

        self_.data = data
