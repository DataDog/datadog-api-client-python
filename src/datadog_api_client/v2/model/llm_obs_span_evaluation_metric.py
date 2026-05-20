# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union

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


class LLMObsSpanEvaluationMetric(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assessment": (str,),
            "eval_metric_type": (str,),
            "reasoning": (str,),
            "status": (str,),
            "tags": ([str],),
            "value": (
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
            ),
        }

    attribute_map = {
        "assessment": "assessment",
        "eval_metric_type": "eval_metric_type",
        "reasoning": "reasoning",
        "status": "status",
        "tags": "tags",
        "value": "value",
    }

    def __init__(
        self_,
        assessment: Union[str, UnsetType] = unset,
        eval_metric_type: Union[str, UnsetType] = unset,
        reasoning: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        value: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        An evaluation metric associated with an LLM Observability span.

        :param assessment: Assessment result (e.g., pass or fail).
        :type assessment: str, optional

        :param eval_metric_type: Type of the evaluation metric (e.g., score, categorical, boolean).
        :type eval_metric_type: str, optional

        :param reasoning: Human-readable reasoning for the evaluation result.
        :type reasoning: str, optional

        :param status: Status of the evaluation execution.
        :type status: str, optional

        :param tags: Tags associated with the evaluation metric.
        :type tags: [str], optional

        :param value: Value of the evaluation result.
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional
        """
        if assessment is not unset:
            kwargs["assessment"] = assessment
        if eval_metric_type is not unset:
            kwargs["eval_metric_type"] = eval_metric_type
        if reasoning is not unset:
            kwargs["reasoning"] = reasoning
        if status is not unset:
            kwargs["status"] = status
        if tags is not unset:
            kwargs["tags"] = tags
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
