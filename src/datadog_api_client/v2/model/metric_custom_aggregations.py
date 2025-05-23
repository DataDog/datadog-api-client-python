# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class MetricCustomAggregations(ModelSimple):
    """
    Deprecated. You no longer need to configure specific time and space aggregations for Metrics Without Limits.


    :type value: [MetricCustomAggregation]
    """

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_custom_aggregation import MetricCustomAggregation

        return {
            "value": ([MetricCustomAggregation],),
        }
