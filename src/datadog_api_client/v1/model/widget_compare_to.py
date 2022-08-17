# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetCompareTo(ModelSimple):
    """
    Timeframe used for the change comparison.

    :param value: Must be one of ["hour_before", "day_before", "week_before", "month_before"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "HOUR_BEFORE": "hour_before",
            "DAY_BEFORE": "day_before",
            "WEEK_BEFORE": "week_before",
            "MONTH_BEFORE": "month_before",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
