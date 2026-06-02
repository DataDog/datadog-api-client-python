# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class AggregatedHighScriptEval(ModelNormal):
    validations = {
        "instance_count": {
            "inclusive_maximum": 2147483647,
        },
        "view_occurrences": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "avg_duration": (int,),
            "avg_forced_style_layout": (int,),
            "fingerprint": (str,),
            "impact_score": (float,),
            "instance_count": (int,),
            "invoker_type": (str,),
            "source_category": (str, none_type),
            "source_function_name": (str,),
            "source_url": (str, none_type),
            "view_occurrences": (int,),
        }

    attribute_map = {
        "avg_duration": "avg_duration",
        "avg_forced_style_layout": "avg_forced_style_layout",
        "fingerprint": "fingerprint",
        "impact_score": "impact_score",
        "instance_count": "instance_count",
        "invoker_type": "invoker_type",
        "source_category": "source_category",
        "source_function_name": "source_function_name",
        "source_url": "source_url",
        "view_occurrences": "view_occurrences",
    }

    def __init__(
        self_,
        avg_duration: int,
        avg_forced_style_layout: int,
        fingerprint: str,
        impact_score: float,
        instance_count: int,
        invoker_type: str,
        source_category: Union[str, none_type],
        source_function_name: str,
        source_url: Union[str, none_type],
        view_occurrences: int,
        **kwargs,
    ):
        """
        Aggregated high script evaluation detection grouped by source.

        :param avg_duration: Average script evaluation duration in nanoseconds.
        :type avg_duration: int

        :param avg_forced_style_layout: Average forced style/layout duration in nanoseconds.
        :type avg_forced_style_layout: int

        :param fingerprint: Unique fingerprint identifying this detection group.
        :type fingerprint: str

        :param impact_score: Impact score combining view frequency and duration severity.
        :type impact_score: float

        :param instance_count: Total number of detection instances across sampled views.
        :type instance_count: int

        :param invoker_type: Type of invoker that triggered the script evaluation.
        :type invoker_type: str

        :param source_category: Category of the script source.
        :type source_category: str, none_type

        :param source_function_name: Name of the function that triggered the high script evaluation.
        :type source_function_name: str

        :param source_url: URL of the script that triggered the high script evaluation.
        :type source_url: str, none_type

        :param view_occurrences: Number of sampled views where this detection occurred.
        :type view_occurrences: int
        """
        super().__init__(kwargs)

        self_.avg_duration = avg_duration
        self_.avg_forced_style_layout = avg_forced_style_layout
        self_.fingerprint = fingerprint
        self_.impact_score = impact_score
        self_.instance_count = instance_count
        self_.invoker_type = invoker_type
        self_.source_category = source_category
        self_.source_function_name = source_function_name
        self_.source_url = source_url
        self_.view_occurrences = view_occurrences
