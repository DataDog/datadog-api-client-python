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
    from datadog_api_client.v2.model.open_ai_usage_and_costs_cloud_cost_data_integration_dataflow_response import (
        OpenAIUsageAndCostsCloudCostDataIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.open_ai_usage_and_costs_usage_metrics_integration_dataflow_response import (
        OpenAIUsageAndCostsUsageMetricsIntegrationDataflowResponse,
    )


class OpenAIUsageAndCostsIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_usage_and_costs_cloud_cost_data_integration_dataflow_response import (
            OpenAIUsageAndCostsCloudCostDataIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.open_ai_usage_and_costs_usage_metrics_integration_dataflow_response import (
            OpenAIUsageAndCostsUsageMetricsIntegrationDataflowResponse,
        )

        return {
            "openai_cloud_cost_data": (OpenAIUsageAndCostsCloudCostDataIntegrationDataflowResponse,),
            "openai_usage_metrics": (OpenAIUsageAndCostsUsageMetricsIntegrationDataflowResponse,),
        }

    attribute_map = {
        "openai_cloud_cost_data": "openai-cloud-cost-data",
        "openai_usage_metrics": "openai-usage-metrics",
    }

    def __init__(
        self_,
        openai_cloud_cost_data: Union[OpenAIUsageAndCostsCloudCostDataIntegrationDataflowResponse, UnsetType] = unset,
        openai_usage_metrics: Union[OpenAIUsageAndCostsUsageMetricsIntegrationDataflowResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from OpenAI Usage and Costs, keyed by dataflow ID.

        :param openai_cloud_cost_data: OpenAI organization costs, which you can analyze in `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. See `collected data <https://docs.datadoghq.com/cloud_cost_management/saas_costs/?tab=openai#data-collected>`_ for what is included.
        :type openai_cloud_cost_data: OpenAIUsageAndCostsCloudCostDataIntegrationDataflowResponse, optional

        :param openai_usage_metrics: Organization usage metrics under the ``openai.*`` namespace, such as ``openai.completions.*`` , ``openai.embeddings.*`` , ``openai.images.*`` , ``openai.moderations.*`` , ``openai.audio_speeches.*`` , ``openai.audio_transcriptions.*`` , ``openai.code_interpreter_sessions.*`` , and ``openai.vector_stores.*``. This dataflow is always on and cannot be turned off, so it appears only in responses.
        :type openai_usage_metrics: OpenAIUsageAndCostsUsageMetricsIntegrationDataflowResponse, optional
        """
        if openai_cloud_cost_data is not unset:
            kwargs["openai_cloud_cost_data"] = openai_cloud_cost_data
        if openai_usage_metrics is not unset:
            kwargs["openai_usage_metrics"] = openai_usage_metrics
        super().__init__(kwargs)
