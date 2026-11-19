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
        Data Datadog collects from OpenAI Codex, keyed by dataflow ID. Datadog always collects daily Codex analytics metrics. Each dataflow in this object adds another type of collection. Set ``enabled`` to start or stop a dataflow. The default for each dataflow applies when the account is created. On update, omitted fields keep their current values. Every dataflow requires an OpenAI enterprise subscription with Codex enabled. If you enable a dataflow without this subscription, Datadog stores the setting but collects no data.

        :param openai_codex_dora: A daily per-engineer engagement signal that `AI Impact <https://docs.datadoghq.com/delivery_performance/ai_impact/>`_ uses to attribute AI-assisted pull requests.
        :type openai_codex_dora: OpenAICodexDoraIntegrationDataflowRequest, optional

        :param openai_codex_turn_metrics: Hourly turn-level metrics from the OpenAI Compliance Logs Platform, including turn and session identity, Work Insights classification, token usage, credits, estimated cost, duration, and activity for skills, plugins, and artifacts. Turn cost is a provider estimate and can differ from invoiced charges. Requires the ``chatgpt.enterprise.compliance_logs_platform.workspace_analytics.read`` scope on the key in ``authentication``. Without this scope, the dataflow collects no data.
        :type openai_codex_turn_metrics: OpenAICodexTurnMetricsIntegrationDataflowRequest, optional
        """
        if openai_codex_dora is not unset:
            kwargs["openai_codex_dora"] = openai_codex_dora
        if openai_codex_turn_metrics is not unset:
            kwargs["openai_codex_turn_metrics"] = openai_codex_turn_metrics
        super().__init__(kwargs)
