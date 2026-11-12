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
    from datadog_api_client.v2.model.open_ai_codex_dora_integration_dataflow_request import (
        OpenAICodexDoraIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.open_ai_codex_turn_metrics_integration_dataflow_request import (
        OpenAICodexTurnMetricsIntegrationDataflowRequest,
    )


class OpenAICodexIntegrationDataflowsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_codex_dora_integration_dataflow_request import (
            OpenAICodexDoraIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.open_ai_codex_turn_metrics_integration_dataflow_request import (
            OpenAICodexTurnMetricsIntegrationDataflowRequest,
        )

        return {
            "openai_codex_dora": (OpenAICodexDoraIntegrationDataflowRequest,),
            "openai_codex_turn_metrics": (OpenAICodexTurnMetricsIntegrationDataflowRequest,),
        }

    attribute_map = {
        "openai_codex_dora": "openai-codex-dora",
        "openai_codex_turn_metrics": "openai-codex-turn-metrics",
    }

    def __init__(
        self_,
        openai_codex_dora: Union[OpenAICodexDoraIntegrationDataflowRequest, UnsetType] = unset,
        openai_codex_turn_metrics: Union[OpenAICodexTurnMetricsIntegrationDataflowRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from OpenAI Codex, keyed by dataflow id. Daily Codex analytics metrics are always collected; each dataflow here adds a further kind of collection on top of that baseline, so set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Every dataflow requires an OpenAI enterprise subscription with Codex enabled; a dataflow enabled without it is stored but collects no data.

        :param openai_codex_dora: A daily per-engineer engagement signal that `AI Impact <https://docs.datadoghq.com/delivery_performance/ai_impact/>`_ uses to attribute AI-assisted pull requests.
        :type openai_codex_dora: OpenAICodexDoraIntegrationDataflowRequest, optional

        :param openai_codex_turn_metrics: Hourly turn-level metrics from the OpenAI Compliance Logs Platform, including turn and session identity, Work Insights classification, token usage, credits, estimated cost, duration, and skill, plugin, and artifact activity. Turn cost is a provider estimate and can differ from invoiced charges. Requires the ``chatgpt.enterprise.compliance_logs_platform.workspace_analytics.read`` scope on the key in ``authentication`` ; without it this dataflow collects no data.
        :type openai_codex_turn_metrics: OpenAICodexTurnMetricsIntegrationDataflowRequest, optional
        """
        if openai_codex_dora is not unset:
            kwargs["openai_codex_dora"] = openai_codex_dora
        if openai_codex_turn_metrics is not unset:
            kwargs["openai_codex_turn_metrics"] = openai_codex_turn_metrics
        super().__init__(kwargs)
