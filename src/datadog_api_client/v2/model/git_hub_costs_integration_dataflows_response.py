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
    from datadog_api_client.v2.model.git_hub_costs_cloud_cost_metrics_integration_dataflow_response import (
        GitHubCostsCloudCostMetricsIntegrationDataflowResponse,
    )


class GitHubCostsIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.git_hub_costs_cloud_cost_metrics_integration_dataflow_response import (
            GitHubCostsCloudCostMetricsIntegrationDataflowResponse,
        )

        return {
            "github_cloud_cost_metrics": (GitHubCostsCloudCostMetricsIntegrationDataflowResponse,),
        }

    attribute_map = {
        "github_cloud_cost_metrics": "github-cloud-cost-metrics",
    }

    def __init__(
        self_,
        github_cloud_cost_metrics: Union[GitHubCostsCloudCostMetricsIntegrationDataflowResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from GitHub Costs, keyed by dataflow ID.

        :param github_cloud_cost_metrics: GitHub costs, including Actions, storage, and Copilot, which you can analyze in `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. Reported costs are estimates based on list prices and usage data and include discounts when available, but not negotiated rates. Requires Cloud Cost Management on your Datadog organization and a GitHub account on the enhanced billing platform. Without them, this dataflow collects no data. This dataflow is always on and cannot be turned off, so it appears in responses only.
        :type github_cloud_cost_metrics: GitHubCostsCloudCostMetricsIntegrationDataflowResponse, optional
        """
        if github_cloud_cost_metrics is not unset:
            kwargs["github_cloud_cost_metrics"] = github_cloud_cost_metrics
        super().__init__(kwargs)
