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
    from datadog_api_client.v2.model.product_analytics_journey_drop_off_response_attributes import (
        ProductAnalyticsJourneyDropOffResponseAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_journey_drop_off_response_type import (
        ProductAnalyticsJourneyDropOffResponseType,
    )


class ProductAnalyticsJourneyDropOffResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_drop_off_response_attributes import (
            ProductAnalyticsJourneyDropOffResponseAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_journey_drop_off_response_type import (
            ProductAnalyticsJourneyDropOffResponseType,
        )

        return {
            "attributes": (ProductAnalyticsJourneyDropOffResponseAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsJourneyDropOffResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsJourneyDropOffResponseAttributes,
        id: str,
        type: ProductAnalyticsJourneyDropOffResponseType,
        **kwargs,
    ):
        """
        The journey drop-off analysis results.

        :param attributes: Attributes of a journey drop-off analysis response.
        :type attributes: ProductAnalyticsJourneyDropOffResponseAttributes

        :param id: Identifier of this result.
        :type id: str

        :param type: The resource type identifier for a journey drop-off analysis response.
        :type type: ProductAnalyticsJourneyDropOffResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
