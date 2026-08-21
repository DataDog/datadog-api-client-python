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
    from datadog_api_client.v2.model.product_analytics_formula_retention_request_attributes import (
        ProductAnalyticsFormulaRetentionRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_formula_retention_request_type import (
        ProductAnalyticsFormulaRetentionRequestType,
    )


class ProductAnalyticsFormulaRetentionRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_formula_retention_request_attributes import (
            ProductAnalyticsFormulaRetentionRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_formula_retention_request_type import (
            ProductAnalyticsFormulaRetentionRequestType,
        )

        return {
            "attributes": (ProductAnalyticsFormulaRetentionRequestAttributes,),
            "type": (ProductAnalyticsFormulaRetentionRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsFormulaRetentionRequestAttributes,
        type: ProductAnalyticsFormulaRetentionRequestType,
        **kwargs,
    ):
        """
        The single JSON:API resource carrying a retention scalar or timeseries query. Its attributes
        hold the time window to query and the retention query definition to evaluate.

        :param attributes: Attributes of a retention scalar or retention timeseries request.
        :type attributes: ProductAnalyticsFormulaRetentionRequestAttributes

        :param type: The resource type identifier for a retention scalar or retention timeseries request.
        :type type: ProductAnalyticsFormulaRetentionRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
