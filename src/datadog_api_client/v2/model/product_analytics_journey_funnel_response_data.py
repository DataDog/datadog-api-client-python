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
    from datadog_api_client.v2.model.product_analytics_journey_funnel_response_attributes import (
        ProductAnalyticsJourneyFunnelResponseAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_journey_funnel_response_type import (
        ProductAnalyticsJourneyFunnelResponseType,
    )


class ProductAnalyticsJourneyFunnelResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_funnel_response_attributes import (
            ProductAnalyticsJourneyFunnelResponseAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_journey_funnel_response_type import (
            ProductAnalyticsJourneyFunnelResponseType,
        )

        return {
            "attributes": (ProductAnalyticsJourneyFunnelResponseAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsJourneyFunnelResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsJourneyFunnelResponseAttributes,
        id: str,
        type: ProductAnalyticsJourneyFunnelResponseType,
        **kwargs,
    ):
        """
        The single JSON:API resource holding a computed funnel. Its attributes contain the number of
        entities that entered, the end-to-end conversion, and one entry per funnel step.

        :param attributes: Attributes of a journey funnel response.
        :type attributes: ProductAnalyticsJourneyFunnelResponseAttributes

        :param id: Identifier of this result.
        :type id: str

        :param type: The resource type identifier for a journey funnel response.
        :type type: ProductAnalyticsJourneyFunnelResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
