# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SplitConfigSortCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aggregation": (str,),
            "metric": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "metric": "metric",
    }

    def __init__(self_, aggregation: str, metric: str, **kwargs):
        """
        Defines the metric and aggregation used as the sort value.

        :param aggregation: How to aggregate the sort metric for the purposes of ordering.
        :type aggregation: str

        :param metric: The metric to use for sorting graphs.
        :type metric: str
        """
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.metric = metric
