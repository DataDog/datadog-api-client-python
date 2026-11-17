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
    from datadog_api_client.v2.model.product_analytics_funnel_step_suggestions_request_attributes import (
        ProductAnalyticsFunnelStepSuggestionsRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_funnel_step_suggestions_request_type import (
        ProductAnalyticsFunnelStepSuggestionsRequestType,
    )


class ProductAnalyticsFunnelStepSuggestionsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_funnel_step_suggestions_request_attributes import (
            ProductAnalyticsFunnelStepSuggestionsRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_funnel_step_suggestions_request_type import (
            ProductAnalyticsFunnelStepSuggestionsRequestType,
        )

        return {
            "attributes": (ProductAnalyticsFunnelStepSuggestionsRequestAttributes,),
            "type": (ProductAnalyticsFunnelStepSuggestionsRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsFunnelStepSuggestionsRequestAttributes,
        type: ProductAnalyticsFunnelStepSuggestionsRequestType,
        **kwargs,
    ):
        """
        Data of a step suggestions request.

        :param attributes: Attributes of a step suggestions request.
        :type attributes: ProductAnalyticsFunnelStepSuggestionsRequestAttributes

        :param type: Type of a step suggestions request.
        :type type: ProductAnalyticsFunnelStepSuggestionsRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
