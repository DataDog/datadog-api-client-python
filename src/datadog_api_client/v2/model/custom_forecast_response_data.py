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
    from datadog_api_client.v2.model.custom_forecast_response_data_attributes import (
        CustomForecastResponseDataAttributes,
    )
    from datadog_api_client.v2.model.custom_forecast_type import CustomForecastType


class CustomForecastResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_forecast_response_data_attributes import (
            CustomForecastResponseDataAttributes,
        )
        from datadog_api_client.v2.model.custom_forecast_type import CustomForecastType

        return {
            "attributes": (CustomForecastResponseDataAttributes,),
            "id": (str,),
            "type": (CustomForecastType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CustomForecastResponseDataAttributes, id: str, type: CustomForecastType, **kwargs):
        """
        Custom forecast resource wrapper in a response.

        :param attributes: Attributes of a custom forecast.
        :type attributes: CustomForecastResponseDataAttributes

        :param id: The unique identifier of the custom forecast.
        :type id: str

        :param type: The type of the custom forecast resource. Must be ``custom_forecast``.
        :type type: CustomForecastType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
