# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class LLMObsCustomEvalConfigAssessmentCriteria(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "max_threshold": (float, none_type),
            "min_threshold": (float, none_type),
            "pass_values": ([str], none_type),
            "pass_when": (bool, none_type),
        }

    attribute_map = {
        "max_threshold": "max_threshold",
        "min_threshold": "min_threshold",
        "pass_values": "pass_values",
        "pass_when": "pass_when",
    }

    def __init__(
        self_,
        max_threshold: Union[float, none_type, UnsetType] = unset,
        min_threshold: Union[float, none_type, UnsetType] = unset,
        pass_values: Union[List[str], none_type, UnsetType] = unset,
        pass_when: Union[bool, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Criteria used to assess the pass/fail result of a custom evaluator.

        :param max_threshold: Maximum numeric threshold for a passing result.
        :type max_threshold: float, none_type, optional

        :param min_threshold: Minimum numeric threshold for a passing result.
        :type min_threshold: float, none_type, optional

        :param pass_values: Specific output values considered as a passing result.
        :type pass_values: [str], none_type, optional

        :param pass_when: When true, a boolean output of true is treated as passing.
        :type pass_when: bool, none_type, optional
        """
        if max_threshold is not unset:
            kwargs["max_threshold"] = max_threshold
        if min_threshold is not unset:
            kwargs["min_threshold"] = min_threshold
        if pass_values is not unset:
            kwargs["pass_values"] = pass_values
        if pass_when is not unset:
            kwargs["pass_when"] = pass_when
        super().__init__(kwargs)
