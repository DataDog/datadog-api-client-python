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
    from datadog_api_client.v2.model.open_ai_codex_dora_integration_dataflow_response import (
        OpenAICodexDoraIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.open_ai_codex_metrics_integration_dataflow_response import (
        OpenAICodexMetricsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.open_ai_codex_turn_metrics_integration_dataflow_response import (
        OpenAICodexTurnMetricsIntegrationDataflowResponse,
    )


class OpenAICodexIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_codex_dora_integration_dataflow_response import (
            OpenAICodexDoraIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.open_ai_codex_metrics_integration_dataflow_response import (
            OpenAICodexMetricsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.open_ai_codex_turn_metrics_integration_dataflow_response import (
            OpenAICodexTurnMetricsIntegrationDataflowResponse,
        )

        return {
            "openai_codex_dora": (OpenAICodexDoraIntegrationDataflowResponse,),
            "openai_codex_metrics": (OpenAICodexMetricsIntegrationDataflowResponse,),
            "openai_codex_turn_metrics": (OpenAICodexTurnMetricsIntegrationDataflowResponse,),
        }

    attribute_map = {
        "openai_codex_dora": "openai-codex-dora",
        "openai_codex_metrics": "openai-codex-metrics",
        "openai_codex_turn_metrics": "openai-codex-turn-metrics",
    }

    def __init__(
        self_,
        openai_codex_dora: Union[OpenAICodexDoraIntegrationDataflowResponse, UnsetType] = unset,
        openai_codex_metrics: Union[OpenAICodexMetricsIntegrationDataflowResponse, UnsetType] = unset,
        openai_codex_turn_metrics: Union[OpenAICodexTurnMetricsIntegrationDataflowResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from OpenAI Codex, keyed by dataflow id.

        :param openai_codex_dora: A daily per-engineer engagement signal that `AI Impact <https://docs.datadoghq.com/delivery_performance/ai_impact/>`_ uses to attribute AI-assisted pull requests.
        :type openai_codex_dora: OpenAICodexDoraIntegrationDataflowResponse, optional

        :param openai_codex_metrics: Daily Codex analytics metrics under the ``openai.codex.*`` namespace: usage totals, token counts by model, thread and turn counts by client, lines of code attributable to Codex, and code reviews. This dataflow is always on and cannot be turned off, which is why it appears in responses only.
        :type openai_codex_metrics: OpenAICodexMetricsIntegrationDataflowResponse, optional

        :param openai_codex_turn_metrics: Hourly turn-level metrics from the OpenAI Compliance Logs Platform, including turn and session identity, Work Insights classification, token usage, credits, estimated cost, duration, and skill, plugin, and artifact activity. Turn cost is a provider estimate and can differ from invoiced charges. Requires the ``chatgpt.enterprise.compliance_logs_platform.workspace_analytics.read`` scope on the key in ``authentication`` ; without it this dataflow collects no data.
        :type openai_codex_turn_metrics: OpenAICodexTurnMetricsIntegrationDataflowResponse, optional
        """
        if openai_codex_dora is not unset:
            kwargs["openai_codex_dora"] = openai_codex_dora
        if openai_codex_metrics is not unset:
            kwargs["openai_codex_metrics"] = openai_codex_metrics
        if openai_codex_turn_metrics is not unset:
            kwargs["openai_codex_turn_metrics"] = openai_codex_turn_metrics
        super().__init__(kwargs)
