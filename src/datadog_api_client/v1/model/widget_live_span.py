# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetLiveSpan(ModelSimple):
    """
    The available timeframes depend on the widget you are using.

    :param value: Must be one of ["1m", "5m", "10m", "15m", "30m", "1h", "4h", "1d", "2d", "1w", "1mo", "3mo", "6mo", "1y", "alert"].
    :type value: str
    """

    allowed_values = {
        "1m",
        "5m",
        "10m",
        "15m",
        "30m",
        "1h",
        "4h",
        "1d",
        "2d",
        "1w",
        "1mo",
        "3mo",
        "6mo",
        "1y",
        "alert",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetLiveSpan.PAST_ONE_MINUTE = WidgetLiveSpan("1m")
WidgetLiveSpan.PAST_FIVE_MINUTES = WidgetLiveSpan("5m")
WidgetLiveSpan.PAST_TEN_MINUTES = WidgetLiveSpan("10m")
WidgetLiveSpan.PAST_FIFTEEN_MINUTES = WidgetLiveSpan("15m")
WidgetLiveSpan.PAST_THIRTY_MINUTES = WidgetLiveSpan("30m")
WidgetLiveSpan.PAST_ONE_HOUR = WidgetLiveSpan("1h")
WidgetLiveSpan.PAST_FOUR_HOURS = WidgetLiveSpan("4h")
WidgetLiveSpan.PAST_ONE_DAY = WidgetLiveSpan("1d")
WidgetLiveSpan.PAST_TWO_DAYS = WidgetLiveSpan("2d")
WidgetLiveSpan.PAST_ONE_WEEK = WidgetLiveSpan("1w")
WidgetLiveSpan.PAST_ONE_MONTH = WidgetLiveSpan("1mo")
WidgetLiveSpan.PAST_THREE_MONTHS = WidgetLiveSpan("3mo")
WidgetLiveSpan.PAST_SIX_MONTHS = WidgetLiveSpan("6mo")
WidgetLiveSpan.PAST_ONE_YEAR = WidgetLiveSpan("1y")
WidgetLiveSpan.ALERT = WidgetLiveSpan("alert")
