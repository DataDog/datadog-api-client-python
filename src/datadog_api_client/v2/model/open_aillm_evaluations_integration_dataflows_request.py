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
    from datadog_api_client.v2.model.open_aillm_evaluations_llm_completions_integration_dataflow_request import (
        OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.open_aillm_evaluations_project_cloud_cost_data_integration_dataflow_request import (
        OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowRequest,
    )


class OpenAILLMEvaluationsIntegrationDataflowsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_aillm_evaluations_llm_completions_integration_dataflow_request import (
            OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.open_aillm_evaluations_project_cloud_cost_data_integration_dataflow_request import (
            OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowRequest,
        )

        return {
            "openai_llm_completions": (OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowRequest,),
            "openai_project_cloud_cost_data": (OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowRequest,),
        }

    attribute_map = {
        "openai_llm_completions": "openai-llm-completions",
        "openai_project_cloud_cost_data": "openai-project-cloud-cost-data",
    }

    def __init__(
        self_,
        openai_llm_completions: Union[OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowRequest, UnsetType] = unset,
        openai_project_cloud_cost_data: Union[
            OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowRequest, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from OpenAI LLM Evaluations, keyed by dataflow ID. Each dataflow turns on a distinct type of collection. Set ``enabled`` to start or stop a dataflow. The default for each dataflow applies when the account is created. On update, omitted fields keep their current values.

        :param openai_llm_completions: Makes the key in ``authentication`` available to run evaluations in `LLM Observability <https://docs.datadoghq.com/llm_observability/>`_. While this dataflow is enabled, a key that cannot call the OpenAI chat completions endpoint is rejected with a ``422`` response.
        :type openai_llm_completions: OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowRequest, optional

        :param openai_project_cloud_cost_data: Costs of the OpenAI project that the key in ``authentication`` belongs to, which you can analyze in `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. Cost data appears in Cloud Cost Management within 24 hours after you enable this dataflow.
        :type openai_project_cloud_cost_data: OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowRequest, optional
        """
        if openai_llm_completions is not unset:
            kwargs["openai_llm_completions"] = openai_llm_completions
        if openai_project_cloud_cost_data is not unset:
            kwargs["openai_project_cloud_cost_data"] = openai_project_cloud_cost_data
        super().__init__(kwargs)
