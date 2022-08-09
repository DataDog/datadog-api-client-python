# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetTimeWindows(ModelSimple):
    """
    Define a time window.

    :param value: Must be one of ["7d", "30d", "90d", "week_to_date", "previous_week", "month_to_date", "previous_month", "global_time"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "SEVEN_DAYS": "7d",
            "THIRTY_DAYS": "30d",
            "NINETY_DAYS": "90d",
            "WEEK_TO_DATE": "week_to_date",
            "PREVIOUS_WEEK": "previous_week",
            "MONTH_TO_DATE": "month_to_date",
            "PREVIOUS_MONTH": "previous_month",
            "GLOBAL_TIME": "global_time",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
