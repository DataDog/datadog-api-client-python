# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardSearchAggregationBucketMultiKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "value": ([str],),
        }

    attribute_map = {
        "count": "count",
        "value": "value",
    }

    def __init__(self_, count: int, value: List[str], **kwargs):
        """
        Aggregation bucket with multiple key values.

        :param count: Number of results in this bucket.
        :type count: int

        :param value: Key values for this bucket.
        :type value: [str]
        """
        super().__init__(kwargs)

        self_.count = count
        self_.value = value
