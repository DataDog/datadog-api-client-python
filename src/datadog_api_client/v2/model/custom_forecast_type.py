# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomForecastType(ModelSimple):
    """
    The type of the custom forecast resource. Must be `custom_forecast`.

    :param value: If omitted defaults to "custom_forecast". Must be one of ["custom_forecast"].
    :type value: str
    """

    allowed_values = {
        "custom_forecast",
    }
    CUSTOM_FORECAST: ClassVar["CustomForecastType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomForecastType.CUSTOM_FORECAST = CustomForecastType("custom_forecast")
