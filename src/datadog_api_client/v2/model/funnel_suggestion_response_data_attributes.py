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
    from datadog_api_client.v2.model.funnel_suggestion_response_data_attributes_actions_items import (
        FunnelSuggestionResponseDataAttributesActionsItems,
    )
    from datadog_api_client.v2.model.funnel_suggestion_response_data_attributes_views_items import (
        FunnelSuggestionResponseDataAttributesViewsItems,
    )


class FunnelSuggestionResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.funnel_suggestion_response_data_attributes_actions_items import (
            FunnelSuggestionResponseDataAttributesActionsItems,
        )
        from datadog_api_client.v2.model.funnel_suggestion_response_data_attributes_views_items import (
            FunnelSuggestionResponseDataAttributesViewsItems,
        )

        return {
            "actions": ([FunnelSuggestionResponseDataAttributesActionsItems],),
            "views": ([FunnelSuggestionResponseDataAttributesViewsItems],),
        }

    attribute_map = {
        "actions": "actions",
        "views": "views",
    }

    def __init__(
        self_,
        actions: Union[List[FunnelSuggestionResponseDataAttributesActionsItems], UnsetType] = unset,
        views: Union[List[FunnelSuggestionResponseDataAttributesViewsItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param actions:
        :type actions: [FunnelSuggestionResponseDataAttributesActionsItems], optional

        :param views:
        :type views: [FunnelSuggestionResponseDataAttributesViewsItems], optional
        """
        if actions is not unset:
            kwargs["actions"] = actions
        if views is not unset:
            kwargs["views"] = views
        super().__init__(kwargs)
