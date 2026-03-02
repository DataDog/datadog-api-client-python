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
    from datadog_api_client.v2.model.llm_obs_experiment_metric_error import LLMObsExperimentMetricError
    from datadog_api_client.v2.model.llm_obs_metric_score_type import LLMObsMetricScoreType


class LLMObsExperimentMetric(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_metric_assessment import LLMObsMetricAssessment
        from datadog_api_client.v2.model.llm_obs_experiment_metric_error import LLMObsExperimentMetricError
        from datadog_api_client.v2.model.llm_obs_metric_score_type import LLMObsMetricScoreType

        return {
            "assessment": (LLMObsMetricAssessment,),
            "boolean_value": (bool,),
            "categorical_value": (str,),
            "error": (LLMObsExperimentMetricError,),
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
            ),
            "metric_type": (LLMObsMetricScoreType,),
            "reasoning": (str,),
            "score_value": (float,),
            "span_id": (str,),
            "tags": ([str],),
            "timestamp_ms": (int,),
        }

    attribute_map = {
        "assessment": "assessment",
        "boolean_value": "boolean_value",
        "categorical_value": "categorical_value",
        "error": "error",
        "json_value": "json_value",
        "label": "label",
        "metadata": "metadata",
        "metric_type": "metric_type",
        "reasoning": "reasoning",
        "score_value": "score_value",
        "span_id": "span_id",
        "tags": "tags",
        "timestamp_ms": "timestamp_ms",
    }

    def __init__(
        self_,
        label: str,
        metric_type: LLMObsMetricScoreType,
        span_id: str,
        timestamp_ms: int,
        assessment: Union[LLMObsMetricAssessment, UnsetType] = unset,
        boolean_value: Union[bool, UnsetType] = unset,
        categorical_value: Union[str, UnsetType] = unset,
        error: Union[LLMObsExperimentMetricError, UnsetType] = unset,
        json_value: Union[Dict[str, Any], UnsetType] = unset,
        metadata: Union[Dict[str, Any], UnsetType] = unset,
        reasoning: Union[str, UnsetType] = unset,
        score_value: Union[float, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        A metric associated with an LLM Observability experiment span.

        :param assessment: Assessment result for an LLM Observability experiment metric.
        :type assessment: LLMObsMetricAssessment, optional

        :param boolean_value: Boolean value. Used when ``metric_type`` is ``boolean``.
        :type boolean_value: bool, optional

        :param categorical_value: Categorical value. Used when ``metric_type`` is ``categorical``.
        :type categorical_value: str, optional

        :param error: Error details for an experiment metric evaluation.
        :type error: LLMObsExperimentMetricError, optional

        :param json_value: JSON value. Used when ``metric_type`` is ``json``.
        :type json_value: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param label: Label or name for the metric.
        :type label: str

        :param metadata: Arbitrary metadata associated with the metric.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param metric_type: Type of metric recorded for an LLM Observability experiment.
        :type metric_type: LLMObsMetricScoreType

        :param reasoning: Human-readable reasoning for the metric value.
        :type reasoning: str, optional

        :param score_value: Numeric score value. Used when ``metric_type`` is ``score``.
        :type score_value: float, optional

        :param span_id: Identifier of the span this metric is associated with.
        :type span_id: str

        :param tags: List of tags associated with the metric.
        :type tags: [str], optional

        :param timestamp_ms: Timestamp when the metric was recorded, in milliseconds since Unix epoch.
        :type timestamp_ms: int
        """
        if assessment is not unset:
            kwargs["assessment"] = assessment
        if boolean_value is not unset:
            kwargs["boolean_value"] = boolean_value
        if categorical_value is not unset:
            kwargs["categorical_value"] = categorical_value
        if error is not unset:
            kwargs["error"] = error
        if json_value is not unset:
            kwargs["json_value"] = json_value
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if reasoning is not unset:
            kwargs["reasoning"] = reasoning
        if score_value is not unset:
            kwargs["score_value"] = score_value
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.label = label
        self_.metric_type = metric_type
        self_.span_id = span_id
        self_.timestamp_ms = timestamp_ms
