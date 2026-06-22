# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_forecast_upsert_request_data_attributes import (
        CustomForecastUpsertRequestDataAttributes,
    )
    from datadog_api_client.v2.model.custom_forecast_type import CustomForecastType


class CustomForecastUpsertRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_forecast_upsert_request_data_attributes import (
            CustomForecastUpsertRequestDataAttributes,
        )
        from datadog_api_client.v2.model.custom_forecast_type import CustomForecastType

        return {
            "attributes": (CustomForecastUpsertRequestDataAttributes,),
            "id": (str,),
            "type": (CustomForecastType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CustomForecastUpsertRequestDataAttributes,
        type: CustomForecastType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Custom forecast resource wrapper in an upsert request.

        :param attributes: Attributes of a custom forecast upsert request.
        :type attributes: CustomForecastUpsertRequestDataAttributes

        :param id: Unused on upsert; the resource is keyed by ``budget_uid``. Send an empty string.
        :type id: str, optional

        :param type: The type of the custom forecast resource. Must be ``custom_forecast``.
        :type type: CustomForecastType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
