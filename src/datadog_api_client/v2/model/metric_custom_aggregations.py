# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class MetricCustomAggregations(ModelSimple):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_custom_aggregation import MetricCustomAggregation

        return {
            "value": ([MetricCustomAggregation],),
        }

    def __init__(self, *args, **kwargs):
        """
        A list of queryable aggregation combinations for a count, rate, or gauge metric.
        By default, count and rate metrics require the (time: sum, space: sum) aggregation and
        Gauge metrics require the (time: avg, space: avg) aggregation.
        Additional time & space combinations are also available:


        * time: avg, space: avg
        * time: avg, space: max
        * time: avg, space: min
        * time: avg, space: sum
        * time: count, space: sum
        * time: max, space: max
        * time: min, space: min
        * time: sum, space: avg
        * time: sum, space: sum

        Can only be applied to metrics that have a ``metric_type`` of ``count`` , ``rate`` , or ``gauge``.

        Note that value can be passed either in args or in kwargs, but not in both.

        :type value: [MetricCustomAggregation]
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=self._path_to_item,
                valid_classes=(self.__class__,),
            )

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
