# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.powerpack_inner_widget_layout import PowerpackInnerWidgetLayout


class PowerpackInnerWidgets(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.powerpack_inner_widget_layout import PowerpackInnerWidgetLayout

        return {
            "definition": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "layout": (PowerpackInnerWidgetLayout,),
        }

    attribute_map = {
        "definition": "definition",
        "layout": "layout",
    }

    def __init__(
        self_, definition: Dict[str, Any], layout: Union[PowerpackInnerWidgetLayout, UnsetType] = unset, **kwargs
    ):
        """
        Powerpack group widget definition of individual widgets.

        :param definition: Information about widget.
        :type definition: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param layout: Powerpack inner widget layout.
        :type layout: PowerpackInnerWidgetLayout, optional
        """
        if layout is not unset:
            kwargs["layout"] = layout
        super().__init__(kwargs)

        self_.definition = definition
