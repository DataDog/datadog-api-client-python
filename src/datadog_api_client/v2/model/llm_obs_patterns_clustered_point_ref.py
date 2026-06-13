# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

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


class LLMObsPatternsClusteredPointRef(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "duration": (float,),
            "estimated_total_cost": (float,),
            "evaluation": (
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
            "input_tokens": (float,),
            "output_tokens": (float,),
            "span_id": (str,),
            "status": (str,),
            "total_tokens": (float,),
        }

    attribute_map = {
        "duration": "duration",
        "estimated_total_cost": "estimated_total_cost",
        "evaluation": "evaluation",
        "input_tokens": "input_tokens",
        "output_tokens": "output_tokens",
        "span_id": "span_id",
        "status": "status",
        "total_tokens": "total_tokens",
    }

    def __init__(
        self_,
        span_id: str,
        duration: Union[float, UnsetType] = unset,
        estimated_total_cost: Union[float, UnsetType] = unset,
        evaluation: Union[Dict[str, Any], UnsetType] = unset,
        input_tokens: Union[float, UnsetType] = unset,
        output_tokens: Union[float, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        total_tokens: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        A clustered point attached inline to a topic. The metric fields are populated
        only when the request includes ``include_metrics=true``.

        :param duration: Duration of the source span in nanoseconds. Included only when metrics are requested.
        :type duration: float, optional

        :param estimated_total_cost: Estimated total cost of the source span. Included only when metrics are requested.
        :type estimated_total_cost: float, optional

        :param evaluation: Evaluation results for the source span keyed by evaluation name. Included
            only when metrics are requested.
        :type evaluation: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param input_tokens: Number of input tokens of the source span. Included only when metrics are requested.
        :type input_tokens: float, optional

        :param output_tokens: Number of output tokens of the source span. Included only when metrics are requested.
        :type output_tokens: float, optional

        :param span_id: Identifier of the source span.
        :type span_id: str

        :param status: Status of the source span. Included only when metrics are requested.
        :type status: str, optional

        :param total_tokens: Total number of tokens of the source span. Included only when metrics are requested.
        :type total_tokens: float, optional
        """
        if duration is not unset:
            kwargs["duration"] = duration
        if estimated_total_cost is not unset:
            kwargs["estimated_total_cost"] = estimated_total_cost
        if evaluation is not unset:
            kwargs["evaluation"] = evaluation
        if input_tokens is not unset:
            kwargs["input_tokens"] = input_tokens
        if output_tokens is not unset:
            kwargs["output_tokens"] = output_tokens
        if status is not unset:
            kwargs["status"] = status
        if total_tokens is not unset:
            kwargs["total_tokens"] = total_tokens
        super().__init__(kwargs)

        self_.span_id = span_id
