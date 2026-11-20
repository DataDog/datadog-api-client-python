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
    from datadog_api_client.v2.model.anthropic_usage_and_costs_cloud_cost_metrics_integration_dataflow_response import (
        AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.anthropic_usage_and_costs_usage_metrics_integration_dataflow_response import (
        AnthropicUsageAndCostsUsageMetricsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.anthropic_usage_and_costs_daily_usage_dora_metrics_integration_dataflow_response import (
        AnthropicUsageAndCostsDailyUsageDoraMetricsIntegrationDataflowResponse,
    )


class AnthropicUsageAndCostsIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.anthropic_usage_and_costs_cloud_cost_metrics_integration_dataflow_response import (
            AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.anthropic_usage_and_costs_usage_metrics_integration_dataflow_response import (
            AnthropicUsageAndCostsUsageMetricsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.anthropic_usage_and_costs_daily_usage_dora_metrics_integration_dataflow_response import (
            AnthropicUsageAndCostsDailyUsageDoraMetricsIntegrationDataflowResponse,
        )

        return {
            "anthropic_cloud_cost_metrics": (AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowResponse,),
            "anthropic_usage_metrics": (AnthropicUsageAndCostsUsageMetricsIntegrationDataflowResponse,),
            "claude_daily_usage_dora_metrics": (
                AnthropicUsageAndCostsDailyUsageDoraMetricsIntegrationDataflowResponse,
            ),
        }

    attribute_map = {
        "anthropic_cloud_cost_metrics": "anthropic-cloud-cost-metrics",
        "anthropic_usage_metrics": "anthropic-usage-metrics",
        "claude_daily_usage_dora_metrics": "claude-daily-usage-dora-metrics",
    }

    def __init__(
        self_,
        anthropic_cloud_cost_metrics: Union[
            AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowResponse, UnsetType
        ] = unset,
        anthropic_usage_metrics: Union[
            AnthropicUsageAndCostsUsageMetricsIntegrationDataflowResponse, UnsetType
        ] = unset,
        claude_daily_usage_dora_metrics: Union[
            AnthropicUsageAndCostsDailyUsageDoraMetricsIntegrationDataflowResponse, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from Anthropic Usage and Costs, keyed by dataflow ID.

        :param anthropic_cloud_cost_metrics: Anthropic costs by model, workspace, and service tier, in `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. Requires Cloud Cost Management on your Datadog organization. Without it, this dataflow collects no data.
        :type anthropic_cloud_cost_metrics: AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowResponse, optional

        :param anthropic_usage_metrics: Anthropic usage metrics, such as input, output, and cache token consumption by model, workspace, and service tier. With an Analytics API key, usage is also broken down by user, product, context window, inference geography, and speed. This dataflow is always on and cannot be turned off, which is why it appears in responses only.
        :type anthropic_usage_metrics: AnthropicUsageAndCostsUsageMetricsIntegrationDataflowResponse, optional

        :param claude_daily_usage_dora_metrics: Daily Claude usage data used for DORA Metrics. This dataflow is always on and cannot be turned off, which is why it appears in responses only.
        :type claude_daily_usage_dora_metrics: AnthropicUsageAndCostsDailyUsageDoraMetricsIntegrationDataflowResponse, optional
        """
        if anthropic_cloud_cost_metrics is not unset:
            kwargs["anthropic_cloud_cost_metrics"] = anthropic_cloud_cost_metrics
        if anthropic_usage_metrics is not unset:
            kwargs["anthropic_usage_metrics"] = anthropic_usage_metrics
        if claude_daily_usage_dora_metrics is not unset:
            kwargs["claude_daily_usage_dora_metrics"] = claude_daily_usage_dora_metrics
        super().__init__(kwargs)
