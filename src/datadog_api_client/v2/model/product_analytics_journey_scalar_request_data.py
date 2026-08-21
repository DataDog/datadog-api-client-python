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
    from datadog_api_client.v2.model.product_analytics_journey_scalar_request_attributes import (
        ProductAnalyticsJourneyScalarRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_formula_journey_request_type import (
        ProductAnalyticsFormulaJourneyRequestType,
    )


class ProductAnalyticsJourneyScalarRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_scalar_request_attributes import (
            ProductAnalyticsJourneyScalarRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_formula_journey_request_type import (
            ProductAnalyticsFormulaJourneyRequestType,
        )

        return {
            "attributes": (ProductAnalyticsJourneyScalarRequestAttributes,),
            "type": (ProductAnalyticsFormulaJourneyRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsJourneyScalarRequestAttributes,
        type: ProductAnalyticsFormulaJourneyRequestType,
        **kwargs,
    ):
        """
        The single JSON:API resource carrying a journey scalar query. Its attributes hold the time
        window and the journey metric to reduce to one value over that window.

        :param attributes: Attributes of a journey scalar request.
        :type attributes: ProductAnalyticsJourneyScalarRequestAttributes

        :param type: The resource type identifier for a journey timeseries or scalar request.
        :type type: ProductAnalyticsFormulaJourneyRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
