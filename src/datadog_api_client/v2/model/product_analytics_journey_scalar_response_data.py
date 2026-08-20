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
    from datadog_api_client.v2.model.product_analytics_scalar_response_attributes import (
        ProductAnalyticsScalarResponseAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_journey_scalar_response_type import (
        ProductAnalyticsJourneyScalarResponseType,
    )


class ProductAnalyticsJourneyScalarResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_scalar_response_attributes import (
            ProductAnalyticsScalarResponseAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_journey_scalar_response_type import (
            ProductAnalyticsJourneyScalarResponseType,
        )

        return {
            "attributes": (ProductAnalyticsScalarResponseAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsJourneyScalarResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsScalarResponseAttributes,
        id: str,
        type: ProductAnalyticsJourneyScalarResponseType,
        **kwargs,
    ):
        """
        The single JSON:API resource holding journey scalar results. Its attributes contain one value
        per group, suitable for a query value or top list widget.

        :param attributes: Attributes of a scalar analytics response, containing the result columns.
        :type attributes: ProductAnalyticsScalarResponseAttributes

        :param id: Identifier of this result.
        :type id: str

        :param type: The resource type identifier for a journey scalar response.
        :type type: ProductAnalyticsJourneyScalarResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
