# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_span_evaluation_metric import LLMObsSpanEvaluationMetric
    from datadog_api_client.v2.model.llm_obs_span_io import LLMObsSpanIO
    from datadog_api_client.v2.model.llm_obs_span_tool_definition import LLMObsSpanToolDefinition


class LLMObsSpanAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_span_evaluation_metric import LLMObsSpanEvaluationMetric
        from datadog_api_client.v2.model.llm_obs_span_io import LLMObsSpanIO
        from datadog_api_client.v2.model.llm_obs_span_tool_definition import LLMObsSpanToolDefinition

        return {
            "duration": (float,),
            "evaluation": ({str: (LLMObsSpanEvaluationMetric,)},),
            "input": (LLMObsSpanIO,),
            "intent": (str,),
            "metadata": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "metrics": ({str: (float,)},),
            "ml_app": (str,),
            "model_name": (str,),
            "model_provider": (str,),
            "name": (str,),
            "output": (LLMObsSpanIO,),
            "parent_id": (str,),
            "span_id": (str,),
            "span_kind": (str,),
            "start_ns": (int,),
            "status": (str,),
            "tags": ([str],),
            "tool_definitions": ([LLMObsSpanToolDefinition],),
            "trace_id": (str,),
        }

    attribute_map = {
        "duration": "duration",
        "evaluation": "evaluation",
        "input": "input",
        "intent": "intent",
        "metadata": "metadata",
        "metrics": "metrics",
        "ml_app": "ml_app",
        "model_name": "model_name",
        "model_provider": "model_provider",
        "name": "name",
        "output": "output",
        "parent_id": "parent_id",
        "span_id": "span_id",
        "span_kind": "span_kind",
        "start_ns": "start_ns",
        "status": "status",
        "tags": "tags",
        "tool_definitions": "tool_definitions",
        "trace_id": "trace_id",
    }

    def __init__(
        self_,
        duration: float,
        ml_app: str,
        name: str,
        span_id: str,
        span_kind: str,
        start_ns: int,
        status: str,
        trace_id: str,
        evaluation: Union[Dict[str, LLMObsSpanEvaluationMetric], UnsetType] = unset,
        input: Union[LLMObsSpanIO, UnsetType] = unset,
        intent: Union[str, UnsetType] = unset,
        metadata: Union[Dict[str, Any], UnsetType] = unset,
        metrics: Union[Dict[str, float], UnsetType] = unset,
        model_name: Union[str, UnsetType] = unset,
        model_provider: Union[str, UnsetType] = unset,
        output: Union[LLMObsSpanIO, UnsetType] = unset,
        parent_id: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        tool_definitions: Union[List[LLMObsSpanToolDefinition], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an LLM Observability span.

        :param duration: Duration of the span in nanoseconds.
        :type duration: float

        :param evaluation: Evaluation metrics keyed by evaluator name.
        :type evaluation: {str: (LLMObsSpanEvaluationMetric,)}, optional

        :param input: Input or output content of an LLM Observability span.
        :type input: LLMObsSpanIO, optional

        :param intent: Detected intent of the span.
        :type intent: str, optional

        :param metadata: Arbitrary metadata associated with the span.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param metrics: Numeric metrics associated with the span (e.g., token counts).
        :type metrics: {str: (float,)}, optional

        :param ml_app: Name of the ML application this span belongs to.
        :type ml_app: str

        :param model_name: Name of the model used in this span.
        :type model_name: str, optional

        :param model_provider: Provider of the model used in this span.
        :type model_provider: str, optional

        :param name: Name of the span.
        :type name: str

        :param output: Input or output content of an LLM Observability span.
        :type output: LLMObsSpanIO, optional

        :param parent_id: Identifier of the parent span, if any.
        :type parent_id: str, optional

        :param span_id: Unique identifier of the span.
        :type span_id: str

        :param span_kind: Kind of span (e.g., llm, agent, tool, task, workflow).
        :type span_kind: str

        :param start_ns: Start time of the span in nanoseconds since Unix epoch.
        :type start_ns: int

        :param status: Status of the span (e.g., ok, error).
        :type status: str

        :param tags: Tags associated with the span.
        :type tags: [str], optional

        :param tool_definitions: Tool definitions available to the span.
        :type tool_definitions: [LLMObsSpanToolDefinition], optional

        :param trace_id: Trace identifier this span belongs to.
        :type trace_id: str
        """
        if evaluation is not unset:
            kwargs["evaluation"] = evaluation
        if input is not unset:
            kwargs["input"] = input
        if intent is not unset:
            kwargs["intent"] = intent
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if model_name is not unset:
            kwargs["model_name"] = model_name
        if model_provider is not unset:
            kwargs["model_provider"] = model_provider
        if output is not unset:
            kwargs["output"] = output
        if parent_id is not unset:
            kwargs["parent_id"] = parent_id
        if tags is not unset:
            kwargs["tags"] = tags
        if tool_definitions is not unset:
            kwargs["tool_definitions"] = tool_definitions
        super().__init__(kwargs)

        self_.duration = duration
        self_.ml_app = ml_app
        self_.name = name
        self_.span_id = span_id
        self_.span_kind = span_kind
        self_.start_ns = start_ns
        self_.status = status
        self_.trace_id = trace_id
