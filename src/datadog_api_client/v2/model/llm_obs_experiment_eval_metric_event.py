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
    from datadog_api_client.v2.model.llm_obs_metric_assessment import LLMObsMetricAssessment
    from datadog_api_client.v2.model.llm_obs_metric_score_type import LLMObsMetricScoreType


class LLMObsExperimentEvalMetricEvent(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_metric_assessment import LLMObsMetricAssessment
        from datadog_api_client.v2.model.llm_obs_metric_score_type import LLMObsMetricScoreType

        return {
            "assessment": (LLMObsMetricAssessment,),
            "boolean_value": (bool, none_type),
            "categorical_value": (str, none_type),
            "eval_source_type": (str,),
            "id": (str,),
            "json_value": (
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
                none_type,
            ),
            "label": (str,),
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
                none_type,
            ),
            "metric_source": (str,),
            "metric_type": (LLMObsMetricScoreType,),
            "reasoning": (str, none_type),
            "score_value": (float, none_type),
            "span_id": (str,),
            "tags": ([str],),
            "timestamp_ms": (int,),
            "trace_id": (str,),
        }

    attribute_map = {
        "assessment": "assessment",
        "boolean_value": "boolean_value",
        "categorical_value": "categorical_value",
        "eval_source_type": "eval_source_type",
        "id": "id",
        "json_value": "json_value",
        "label": "label",
        "metadata": "metadata",
        "metric_source": "metric_source",
        "metric_type": "metric_type",
        "reasoning": "reasoning",
        "score_value": "score_value",
        "span_id": "span_id",
        "tags": "tags",
        "timestamp_ms": "timestamp_ms",
        "trace_id": "trace_id",
    }

    def __init__(
        self_,
        assessment: Union[LLMObsMetricAssessment, UnsetType] = unset,
        boolean_value: Union[bool, none_type, UnsetType] = unset,
        categorical_value: Union[str, none_type, UnsetType] = unset,
        eval_source_type: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        json_value: Union[Dict[str, Any], none_type, UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        metadata: Union[Dict[str, Any], none_type, UnsetType] = unset,
        metric_source: Union[str, UnsetType] = unset,
        metric_type: Union[LLMObsMetricScoreType, UnsetType] = unset,
        reasoning: Union[str, none_type, UnsetType] = unset,
        score_value: Union[float, none_type, UnsetType] = unset,
        span_id: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        timestamp_ms: Union[int, UnsetType] = unset,
        trace_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        An evaluation metric event associated with an experiment span.

        :param assessment: Assessment result for an LLM Observability experiment metric.
        :type assessment: LLMObsMetricAssessment, optional

        :param boolean_value: Boolean value. Present when ``metric_type`` is ``boolean``.
        :type boolean_value: bool, none_type, optional

        :param categorical_value: Categorical value. Present when ``metric_type`` is ``categorical``.
        :type categorical_value: str, none_type, optional

        :param eval_source_type: Source type of the evaluation.
        :type eval_source_type: str, optional

        :param id: Unique identifier of the evaluation metric event.
        :type id: str, optional

        :param json_value: JSON value. Present when ``metric_type`` is ``json``.
        :type json_value: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param label: Label or name for the metric.
        :type label: str, optional

        :param metadata: Arbitrary metadata associated with the metric.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param metric_source: Source of the metric. Either ``custom`` (user-submitted) or ``summary`` (experiment-level aggregate).
        :type metric_source: str, optional

        :param metric_type: Type of metric recorded for an LLM Observability experiment.
        :type metric_type: LLMObsMetricScoreType, optional

        :param reasoning: Human-readable reasoning for the metric value.
        :type reasoning: str, none_type, optional

        :param score_value: Numeric score. Present when ``metric_type`` is ``score``.
        :type score_value: float, none_type, optional

        :param span_id: Span ID this metric is associated with.
        :type span_id: str, optional

        :param tags: Tags associated with the metric.
        :type tags: [str], optional

        :param timestamp_ms: Timestamp when the metric was recorded, in milliseconds since Unix epoch.
        :type timestamp_ms: int, optional

        :param trace_id: Trace ID linking this metric to a span.
        :type trace_id: str, optional
        """
        if assessment is not unset:
            kwargs["assessment"] = assessment
        if boolean_value is not unset:
            kwargs["boolean_value"] = boolean_value
        if categorical_value is not unset:
            kwargs["categorical_value"] = categorical_value
        if eval_source_type is not unset:
            kwargs["eval_source_type"] = eval_source_type
        if id is not unset:
            kwargs["id"] = id
        if json_value is not unset:
            kwargs["json_value"] = json_value
        if label is not unset:
            kwargs["label"] = label
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if metric_source is not unset:
            kwargs["metric_source"] = metric_source
        if metric_type is not unset:
            kwargs["metric_type"] = metric_type
        if reasoning is not unset:
            kwargs["reasoning"] = reasoning
        if score_value is not unset:
            kwargs["score_value"] = score_value
        if span_id is not unset:
            kwargs["span_id"] = span_id
        if tags is not unset:
            kwargs["tags"] = tags
        if timestamp_ms is not unset:
            kwargs["timestamp_ms"] = timestamp_ms
        if trace_id is not unset:
            kwargs["trace_id"] = trace_id
        super().__init__(kwargs)
