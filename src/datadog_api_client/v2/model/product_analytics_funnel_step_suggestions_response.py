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
    from datadog_api_client.v2.model.product_analytics_funnel_step_suggestions_response_data import (
        ProductAnalyticsFunnelStepSuggestionsResponseData,
    )


class ProductAnalyticsFunnelStepSuggestionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_funnel_step_suggestions_response_data import (
            ProductAnalyticsFunnelStepSuggestionsResponseData,
        )

        return {
            "data": (ProductAnalyticsFunnelStepSuggestionsResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsFunnelStepSuggestionsResponseData, **kwargs):
        """
        Suggested next steps for a funnel.

        :param data: Data of a step suggestions response.
        :type data: ProductAnalyticsFunnelStepSuggestionsResponseData
        """
        super().__init__(kwargs)

        self_.data = data
