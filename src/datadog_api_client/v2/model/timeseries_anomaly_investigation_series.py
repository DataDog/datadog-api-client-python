# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TimeseriesAnomalyInvestigationSeries(ModelNormal):
    validations = {
        "query_index": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "group_tags": ([str],),
            "label": (str,),
            "query_index": (int,),
        }

    attribute_map = {
        "group_tags": "group_tags",
        "label": "label",
        "query_index": "query_index",
    }

    def __init__(self_, group_tags: List[str], label: str, query_index: int, **kwargs):
        """
        Logical series on which the anomaly was detected.

        :param group_tags: Tags identifying the selected group. Empty for a query without grouping.
        :type group_tags: [str]

        :param label: Display label for the selected series.
        :type label: str

        :param query_index: Zero-based index of the caller's formula that produced the series.
        :type query_index: int
        """
        super().__init__(kwargs)

        self_.group_tags = group_tags
        self_.label = label
        self_.query_index = query_index
