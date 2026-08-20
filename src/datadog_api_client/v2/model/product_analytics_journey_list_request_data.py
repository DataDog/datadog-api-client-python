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
    from datadog_api_client.v2.model.product_analytics_journey_list_request_attributes import (
        ProductAnalyticsJourneyListRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_journey_list_request_type import (
        ProductAnalyticsJourneyListRequestType,
    )


class ProductAnalyticsJourneyListRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_list_request_attributes import (
            ProductAnalyticsJourneyListRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_journey_list_request_type import (
            ProductAnalyticsJourneyListRequestType,
        )

        return {
            "attributes": (ProductAnalyticsJourneyListRequestAttributes,),
            "type": (ProductAnalyticsJourneyListRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsJourneyListRequestAttributes,
        type: ProductAnalyticsJourneyListRequestType,
        **kwargs,
    ):
        """
        The single JSON:API resource carrying a journey list query. Its attributes hold the time window
        and the journey whose matching entities should be listed, one row each.

        :param attributes: Attributes of a journey list request.
        :type attributes: ProductAnalyticsJourneyListRequestAttributes

        :param type: The resource type identifier for a journey list request.
        :type type: ProductAnalyticsJourneyListRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
