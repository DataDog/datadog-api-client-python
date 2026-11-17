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
    from datadog_api_client.v2.model.product_analytics_journey_drop_off_request_attributes import (
        ProductAnalyticsJourneyDropOffRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_journey_drop_off_request_type import (
        ProductAnalyticsJourneyDropOffRequestType,
    )


class ProductAnalyticsJourneyDropOffRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_drop_off_request_attributes import (
            ProductAnalyticsJourneyDropOffRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_journey_drop_off_request_type import (
            ProductAnalyticsJourneyDropOffRequestType,
        )

        return {
            "attributes": (ProductAnalyticsJourneyDropOffRequestAttributes,),
            "type": (ProductAnalyticsJourneyDropOffRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsJourneyDropOffRequestAttributes,
        type: ProductAnalyticsJourneyDropOffRequestType,
        **kwargs,
    ):
        """
        The definition of a journey drop-off analysis request body.

        :param attributes: Attributes of a journey drop-off analysis request.
        :type attributes: ProductAnalyticsJourneyDropOffRequestAttributes

        :param type: The resource type identifier for a journey drop-off analysis request.
        :type type: ProductAnalyticsJourneyDropOffRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
