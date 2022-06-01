# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class MetricEstimateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_estimate_type import MetricEstimateType

        return {
            "estimate_type": (MetricEstimateType,),
            "estimated_at": (datetime,),
            "estimated_output_series": (int,),
        }

    attribute_map = {
        "estimate_type": "estimate_type",
        "estimated_at": "estimated_at",
        "estimated_output_series": "estimated_output_series",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing the definition of a metric estimate attribute.

        :param estimate_type: Estimate type based on the queried configuration. By default, ``count_or_gauge`` is returned. ``distribution`` is returned for distribution metrics without percentiles enabled. Lastly, ``percentile`` is returned if ``filter[pct]=true`` is queried with a distribution metric.
        :type estimate_type: MetricEstimateType, optional

        :param estimated_at: Timestamp when the cardinality estimate was requested.
        :type estimated_at: datetime, optional

        :param estimated_output_series: Estimated cardinality of the metric based on the queried configuration.
        :type estimated_output_series: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricEstimateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
