# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ScoreResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aggregation": (str,),
            "denominator": (int,),
            "numerator": (int,),
            "score": (float,),
            "total_fail": (int,),
            "total_no_data": (int,),
            "total_pass": (int,),
            "total_skip": (int,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "denominator": "denominator",
        "numerator": "numerator",
        "score": "score",
        "total_fail": "total_fail",
        "total_no_data": "total_no_data",
        "total_pass": "total_pass",
        "total_skip": "total_skip",
    }

    def __init__(
        self_,
        aggregation: str,
        denominator: int,
        numerator: int,
        score: float,
        total_fail: int,
        total_no_data: int,
        total_pass: int,
        total_skip: int,
        **kwargs,
    ):
        """
        Score attributes.

        :param aggregation: The aggregation type.
        :type aggregation: str

        :param denominator: Score denominator.
        :type denominator: int

        :param numerator: Score numerator.
        :type numerator: int

        :param score: Calculated score value.
        :type score: float

        :param total_fail: Total number of failing rules.
        :type total_fail: int

        :param total_no_data: Total number of rules with no data.
        :type total_no_data: int

        :param total_pass: Total number of passing rules.
        :type total_pass: int

        :param total_skip: Total number of skipped rules.
        :type total_skip: int
        """
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.denominator = denominator
        self_.numerator = numerator
        self_.score = score
        self_.total_fail = total_fail
        self_.total_no_data = total_no_data
        self_.total_pass = total_pass
        self_.total_skip = total_skip
