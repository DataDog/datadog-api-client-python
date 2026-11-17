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
    from datadog_api_client.v2.model.product_analytics_funnel_suggestions_feature import (
        ProductAnalyticsFunnelSuggestionsFeature,
    )


class ProductAnalyticsFunnelSuggestionsDomain(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_funnel_suggestions_feature import (
            ProductAnalyticsFunnelSuggestionsFeature,
        )

        return {
            "features": ([ProductAnalyticsFunnelSuggestionsFeature],),
            "name": (str,),
        }

    attribute_map = {
        "features": "features",
        "name": "name",
    }

    def __init__(
        self_,
        features: Union[List[ProductAnalyticsFunnelSuggestionsFeature], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A feature area of an application, such as checkout or settings.

        :param features: Features in this area.
        :type features: [ProductAnalyticsFunnelSuggestionsFeature], optional

        :param name: Name of the feature area.
        :type name: str, optional
        """
        if features is not unset:
            kwargs["features"] = features
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
