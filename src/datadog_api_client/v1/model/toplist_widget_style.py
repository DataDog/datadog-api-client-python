# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.toplist_widget_display import ToplistWidgetDisplay
    from datadog_api_client.v1.model.toplist_widget_scaling import ToplistWidgetScaling
    from datadog_api_client.v1.model.toplist_widget_stacked import ToplistWidgetStacked
    from datadog_api_client.v1.model.toplist_widget_flat import ToplistWidgetFlat


class ToplistWidgetStyle(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.toplist_widget_display import ToplistWidgetDisplay
        from datadog_api_client.v1.model.toplist_widget_scaling import ToplistWidgetScaling

        return {
            "display": (ToplistWidgetDisplay,),
            "scaling": (ToplistWidgetScaling,),
        }

    attribute_map = {
        "display": "display",
        "scaling": "scaling",
    }

    def __init__(
        self_,
        display: Union[ToplistWidgetDisplay, ToplistWidgetStacked, ToplistWidgetFlat, UnsetType] = unset,
        scaling: Union[ToplistWidgetScaling, UnsetType] = unset,
        **kwargs,
    ):
        """
        Style customization for a top list widget.

        :param display: Top list widget display options.
        :type display: ToplistWidgetDisplay, optional

        :param scaling: Top list widget scaling definition.
        :type scaling: ToplistWidgetScaling, optional
        """
        if display is not unset:
            kwargs["display"] = display
        if scaling is not unset:
            kwargs["scaling"] = scaling
        super().__init__(kwargs)
