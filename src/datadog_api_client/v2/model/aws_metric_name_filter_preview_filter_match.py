# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSMetricNameFilterPreviewFilterMatch(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "match_count": (int,),
            "pattern": (str,),
        }

    attribute_map = {
        "match_count": "match_count",
        "pattern": "pattern",
    }

    def __init__(self_, match_count: int, pattern: str, **kwargs):
        """
        A metric name filter pattern and how many metrics it matched.

        :param match_count: The number of Datadog metric names matched by this pattern.
        :type match_count: int

        :param pattern: The metric name filter pattern.
        :type pattern: str
        """
        super().__init__(kwargs)

        self_.match_count = match_count
        self_.pattern = pattern
