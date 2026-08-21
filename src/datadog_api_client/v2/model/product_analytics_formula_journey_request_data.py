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
    from datadog_api_client.v2.model.product_analytics_formula_journey_request_attributes import (
        ProductAnalyticsFormulaJourneyRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_formula_journey_request_type import (
        ProductAnalyticsFormulaJourneyRequestType,
    )


class ProductAnalyticsFormulaJourneyRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_formula_journey_request_attributes import (
            ProductAnalyticsFormulaJourneyRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_formula_journey_request_type import (
            ProductAnalyticsFormulaJourneyRequestType,
        )

        return {
            "attributes": (ProductAnalyticsFormulaJourneyRequestAttributes,),
            "type": (ProductAnalyticsFormulaJourneyRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsFormulaJourneyRequestAttributes,
        type: ProductAnalyticsFormulaJourneyRequestType,
        **kwargs,
    ):
        """
        The single JSON:API resource carrying a journey timeseries query. Its attributes hold the time
        window, the bucket interval that splits it, and the journey metric to compute per bucket.

        :param attributes: Attributes of a journey timeseries request.
        :type attributes: ProductAnalyticsFormulaJourneyRequestAttributes

        :param type: The resource type identifier for a journey timeseries or scalar request.
        :type type: ProductAnalyticsFormulaJourneyRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
