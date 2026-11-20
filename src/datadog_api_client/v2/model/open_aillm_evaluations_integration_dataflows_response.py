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
    from datadog_api_client.v2.model.open_aillm_evaluations_llm_completions_integration_dataflow_response import (
        OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.open_aillm_evaluations_project_cloud_cost_data_integration_dataflow_response import (
        OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowResponse,
    )


class OpenAILLMEvaluationsIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_aillm_evaluations_llm_completions_integration_dataflow_response import (
            OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.open_aillm_evaluations_project_cloud_cost_data_integration_dataflow_response import (
            OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowResponse,
        )

        return {
            "openai_llm_completions": (OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowResponse,),
            "openai_project_cloud_cost_data": (OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowResponse,),
        }

    attribute_map = {
        "openai_llm_completions": "openai-llm-completions",
        "openai_project_cloud_cost_data": "openai-project-cloud-cost-data",
    }

    def __init__(
        self_,
        openai_llm_completions: Union[OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowResponse, UnsetType] = unset,
        openai_project_cloud_cost_data: Union[
            OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowResponse, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from OpenAI LLM Evaluations, keyed by dataflow ID.

        :param openai_llm_completions: Makes the key in ``authentication`` available to run evaluations in `LLM Observability <https://docs.datadoghq.com/llm_observability/>`_.
        :type openai_llm_completions: OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowResponse, optional

        :param openai_project_cloud_cost_data: Costs of the OpenAI project that the key in ``authentication`` belongs to, which you can analyze in `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_.
        :type openai_project_cloud_cost_data: OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowResponse, optional
        """
        if openai_llm_completions is not unset:
            kwargs["openai_llm_completions"] = openai_llm_completions
        if openai_project_cloud_cost_data is not unset:
            kwargs["openai_project_cloud_cost_data"] = openai_project_cloud_cost_data
        super().__init__(kwargs)
