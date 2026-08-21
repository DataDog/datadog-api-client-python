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
    from datadog_api_client.v2.model.product_analytics_journey_list_response_attributes import (
        ProductAnalyticsJourneyListResponseAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_journey_list_response_type import (
        ProductAnalyticsJourneyListResponseType,
    )


class ProductAnalyticsJourneyListResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_list_response_attributes import (
            ProductAnalyticsJourneyListResponseAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_journey_list_response_type import (
            ProductAnalyticsJourneyListResponseType,
        )

        return {
            "attributes": (ProductAnalyticsJourneyListResponseAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsJourneyListResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsJourneyListResponseAttributes,
        id: str,
        type: ProductAnalyticsJourneyListResponseType,
        **kwargs,
    ):
        """
        The single JSON:API resource holding the entities matching a journey. Its attributes contain
        the returned rows and the total number of rows that matched, ignoring ``limit``.

        :param attributes: Attributes of a journey list response.
        :type attributes: ProductAnalyticsJourneyListResponseAttributes

        :param id: Identifier of this result.
        :type id: str

        :param type: The resource type identifier for a journey list response.
        :type type: ProductAnalyticsJourneyListResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
