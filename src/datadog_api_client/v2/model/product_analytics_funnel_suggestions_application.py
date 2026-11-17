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
    from datadog_api_client.v2.model.product_analytics_funnel_suggestions_domain import (
        ProductAnalyticsFunnelSuggestionsDomain,
    )


class ProductAnalyticsFunnelSuggestionsApplication(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_funnel_suggestions_domain import (
            ProductAnalyticsFunnelSuggestionsDomain,
        )

        return {
            "application_id": (str,),
            "domains": ([ProductAnalyticsFunnelSuggestionsDomain],),
        }

    attribute_map = {
        "application_id": "application_id",
        "domains": "domains",
    }

    def __init__(
        self_,
        application_id: Union[str, UnsetType] = unset,
        domains: Union[List[ProductAnalyticsFunnelSuggestionsDomain], UnsetType] = unset,
        **kwargs,
    ):
        """
        Suggested features of one application.

        :param application_id: ID of the RUM application.
        :type application_id: str, optional

        :param domains: Feature areas of the application.
        :type domains: [ProductAnalyticsFunnelSuggestionsDomain], optional
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        if domains is not unset:
            kwargs["domains"] = domains
        super().__init__(kwargs)
