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
    from datadog_api_client.v2.model.product_analytics_journey_funnel_request_attributes import (
        ProductAnalyticsJourneyFunnelRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_journey_request_type import ProductAnalyticsJourneyRequestType


class ProductAnalyticsJourneyFunnelRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_funnel_request_attributes import (
            ProductAnalyticsJourneyFunnelRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_journey_request_type import (
            ProductAnalyticsJourneyRequestType,
        )

        return {
            "attributes": (ProductAnalyticsJourneyFunnelRequestAttributes,),
            "type": (ProductAnalyticsJourneyRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsJourneyFunnelRequestAttributes,
        type: ProductAnalyticsJourneyRequestType,
        **kwargs,
    ):
        """
        The single JSON:API resource carrying a funnel query. Its attributes hold the time window to
        query and the journey whose step-to-step conversion should be measured.

        :param attributes: Attributes of a journey funnel request.
        :type attributes: ProductAnalyticsJourneyFunnelRequestAttributes

        :param type: The resource type identifier for a journey funnel request.
        :type type: ProductAnalyticsJourneyRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
