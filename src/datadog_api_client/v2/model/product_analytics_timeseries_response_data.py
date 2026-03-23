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
    from datadog_api_client.v2.model.product_analytics_timeseries_response_attributes import (
        ProductAnalyticsTimeseriesResponseAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_timeseries_response_type import (
        ProductAnalyticsTimeseriesResponseType,
    )


class ProductAnalyticsTimeseriesResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_timeseries_response_attributes import (
            ProductAnalyticsTimeseriesResponseAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_timeseries_response_type import (
            ProductAnalyticsTimeseriesResponseType,
        )

        return {
            "attributes": (ProductAnalyticsTimeseriesResponseAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsTimeseriesResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ProductAnalyticsTimeseriesResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[ProductAnalyticsTimeseriesResponseType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a timeseries analytics response.

        :param attributes: Attributes of a timeseries analytics response, containing series data, timestamps, and interval definitions.
        :type attributes: ProductAnalyticsTimeseriesResponseAttributes, optional

        :param id: Unique identifier for this response data object.
        :type id: str, optional

        :param type: The resource type identifier for a timeseries analytics response.
        :type type: ProductAnalyticsTimeseriesResponseType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
