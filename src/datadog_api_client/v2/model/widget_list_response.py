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
    from datadog_api_client.v2.model.widget_data import WidgetData
    from datadog_api_client.v2.model.widget_included_user import WidgetIncludedUser
    from datadog_api_client.v2.model.widget_search_meta import WidgetSearchMeta


class WidgetListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.widget_data import WidgetData
        from datadog_api_client.v2.model.widget_included_user import WidgetIncludedUser
        from datadog_api_client.v2.model.widget_search_meta import WidgetSearchMeta

        return {
            "data": ([WidgetData],),
            "included": ([WidgetIncludedUser],),
            "meta": (WidgetSearchMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[WidgetData],
        included: Union[List[WidgetIncludedUser], UnsetType] = unset,
        meta: Union[WidgetSearchMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a list of widgets.

        :param data: List of widget resources.
        :type data: [WidgetData]

        :param included: Array of user resources related to the widgets.
        :type included: [WidgetIncludedUser], optional

        :param meta: Metadata about the search results.
        :type meta: WidgetSearchMeta, optional
        """
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
