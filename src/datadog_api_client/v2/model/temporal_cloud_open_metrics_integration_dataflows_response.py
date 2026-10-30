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
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_metrics_integration_dataflow_response import (
        TemporalCloudOpenMetricsMetricsIntegrationDataflowResponse,
    )


class TemporalCloudOpenMetricsIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporal_cloud_open_metrics_metrics_integration_dataflow_response import (
            TemporalCloudOpenMetricsMetricsIntegrationDataflowResponse,
        )

        return {
            "temporal_cloud_openmetrics_metrics": (TemporalCloudOpenMetricsMetricsIntegrationDataflowResponse,),
        }

    attribute_map = {
        "temporal_cloud_openmetrics_metrics": "temporal-cloud-openmetrics-metrics",
    }

    def __init__(
        self_,
        temporal_cloud_openmetrics_metrics: Union[
            TemporalCloudOpenMetricsMetricsIntegrationDataflowResponse, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from Temporal Cloud OpenMetrics, keyed by dataflow id.

        :param temporal_cloud_openmetrics_metrics: Temporal Cloud operational metrics for your namespaces, workflows and task queues, such as workflow and activity rates, task polling, and service request latency, collected from Temporal Cloud's OpenMetrics endpoint. This is the integration's only collection: it is always on and cannot be turned off, which is why it appears in responses only.
        :type temporal_cloud_openmetrics_metrics: TemporalCloudOpenMetricsMetricsIntegrationDataflowResponse, optional
        """
        if temporal_cloud_openmetrics_metrics is not unset:
            kwargs["temporal_cloud_openmetrics_metrics"] = temporal_cloud_openmetrics_metrics
        super().__init__(kwargs)
