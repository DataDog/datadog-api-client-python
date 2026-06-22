# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_forecast_response_data import CustomForecastResponseData


class CustomForecastResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_forecast_response_data import CustomForecastResponseData

        return {
            "data": (CustomForecastResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CustomForecastResponseData, **kwargs):
        """
        Response object containing the custom forecast for a budget.

        :param data: Custom forecast resource wrapper in a response.
        :type data: CustomForecastResponseData
        """
        super().__init__(kwargs)

        self_.data = data
