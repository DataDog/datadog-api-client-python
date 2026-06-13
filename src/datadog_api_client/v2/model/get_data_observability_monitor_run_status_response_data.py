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
    from datadog_api_client.v2.model.get_data_observability_monitor_run_status_response_attributes import (
        GetDataObservabilityMonitorRunStatusResponseAttributes,
    )
    from datadog_api_client.v2.model.data_observability_monitor_run_type import DataObservabilityMonitorRunType


class GetDataObservabilityMonitorRunStatusResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_data_observability_monitor_run_status_response_attributes import (
            GetDataObservabilityMonitorRunStatusResponseAttributes,
        )
        from datadog_api_client.v2.model.data_observability_monitor_run_type import DataObservabilityMonitorRunType

        return {
            "attributes": (GetDataObservabilityMonitorRunStatusResponseAttributes,),
            "id": (str,),
            "type": (DataObservabilityMonitorRunType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GetDataObservabilityMonitorRunStatusResponseAttributes,
        id: str,
        type: DataObservabilityMonitorRunType,
        **kwargs,
    ):
        """
        The data object for a data observability monitor run status response.

        :param attributes: The attributes of a data observability monitor run status response.
        :type attributes: GetDataObservabilityMonitorRunStatusResponseAttributes

        :param id: The unique identifier of the monitor run.
        :type id: str

        :param type: The JSON:API resource type for a data observability monitor run.
        :type type: DataObservabilityMonitorRunType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
