# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class HeatgridLegend(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "show_caption": (bool,),
        }

    attribute_map = {
        "show_caption": "show_caption",
    }

    def __init__(self_, show_caption: Union[bool, UnsetType] = unset, **kwargs):
        """
        Legend configuration for the heatgrid widget.

        :param show_caption: Whether to display the legend caption.
        :type show_caption: bool, optional
        """
        if show_caption is not unset:
            kwargs["show_caption"] = show_caption
        super().__init__(kwargs)
