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


class WidgetResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.widget_data import WidgetData
        from datadog_api_client.v2.model.widget_included_user import WidgetIncludedUser

        return {
            "data": (WidgetData,),
            "included": ([WidgetIncludedUser],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(self_, data: WidgetData, included: Union[List[WidgetIncludedUser], UnsetType] = unset, **kwargs):
        """
        Response containing a single widget.

        :param data: A widget resource object.
        :type data: WidgetData

        :param included: Array of user resources related to the widget.
        :type included: [WidgetIncludedUser], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
