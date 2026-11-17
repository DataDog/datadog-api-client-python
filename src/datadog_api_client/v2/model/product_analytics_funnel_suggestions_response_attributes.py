# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_funnel_suggestions_application import (
        ProductAnalyticsFunnelSuggestionsApplication,
    )


class ProductAnalyticsFunnelSuggestionsResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_funnel_suggestions_application import (
            ProductAnalyticsFunnelSuggestionsApplication,
        )

        return {
            "applications": ([ProductAnalyticsFunnelSuggestionsApplication],),
        }

    attribute_map = {
        "applications": "applications",
    }

    def __init__(
        self_, applications: Union[List[ProductAnalyticsFunnelSuggestionsApplication], UnsetType] = unset, **kwargs
    ):
        """
        Attributes of a feature suggestions response.

        :param applications: Suggested features, grouped by application and feature area.
        :type applications: [ProductAnalyticsFunnelSuggestionsApplication], optional
        """
        if applications is not unset:
            kwargs["applications"] = applications
        super().__init__(kwargs)
