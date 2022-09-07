# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetAggregator(ModelSimple):
    """
    Aggregator used for the request.

    :param value: Must be one of ["avg", "last", "max", "min", "sum", "percentile"].
    :type value: str
    """

    allowed_values = {
        "avg",
        "last",
        "max",
        "min",
        "sum",
        "percentile",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetAggregator.AVERAGE = WidgetAggregator("avg")
WidgetAggregator.LAST = WidgetAggregator("last")
WidgetAggregator.MAXIMUM = WidgetAggregator("max")
WidgetAggregator.MINIMUM = WidgetAggregator("min")
WidgetAggregator.SUM = WidgetAggregator("sum")
WidgetAggregator.PERCENTILE = WidgetAggregator("percentile")
