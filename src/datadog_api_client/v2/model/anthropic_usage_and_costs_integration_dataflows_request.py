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
    from datadog_api_client.v2.model.anthropic_usage_and_costs_cloud_cost_metrics_integration_dataflow_request import (
        AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowRequest,
    )


class AnthropicUsageAndCostsIntegrationDataflowsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.anthropic_usage_and_costs_cloud_cost_metrics_integration_dataflow_request import (
            AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowRequest,
        )

        return {
            "anthropic_cloud_cost_metrics": (AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowRequest,),
        }

    attribute_map = {
        "anthropic_cloud_cost_metrics": "anthropic-cloud-cost-metrics",
    }

    def __init__(
        self_,
        anthropic_cloud_cost_metrics: Union[
            AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowRequest, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from Anthropic Usage and Costs, keyed by dataflow ID. Datadog always collects usage metrics. Each dataflow in this object adds another type of collection. Set ``enabled`` to start or stop a dataflow. The default for each dataflow applies when the account is created. On update, omitted fields keep their current values. If a dataflow depends on a Datadog product, its description names that product. If you enable a dataflow without that product, Datadog stores the setting but collects no data.

        :param anthropic_cloud_cost_metrics: Anthropic costs by model, workspace, and service tier, in `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. Requires Cloud Cost Management on your Datadog organization. Without it, this dataflow collects no data. Cost data appears in Cloud Cost Management within 24 to 48 hours of enabling this dataflow.
        :type anthropic_cloud_cost_metrics: AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowRequest, optional
        """
        if anthropic_cloud_cost_metrics is not unset:
            kwargs["anthropic_cloud_cost_metrics"] = anthropic_cloud_cost_metrics
        super().__init__(kwargs)
