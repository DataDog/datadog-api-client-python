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
    from datadog_api_client.v1.model.heatgrid_text_format_rule import HeatgridTextFormatRule
    from datadog_api_client.v1.model.heatgrid_label_column_width import HeatgridLabelColumnWidth


class HeatgridLabelColumn(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_text_format_rule import HeatgridTextFormatRule
        from datadog_api_client.v1.model.heatgrid_label_column_width import HeatgridLabelColumnWidth

        return {
            "text_formats": ([HeatgridTextFormatRule],),
            "width": (HeatgridLabelColumnWidth,),
        }

    attribute_map = {
        "text_formats": "text_formats",
        "width": "width",
    }

    def __init__(
        self_,
        text_formats: Union[List[HeatgridTextFormatRule], UnsetType] = unset,
        width: Union[HeatgridLabelColumnWidth, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration of the group label column. Its width is sized automatically when omitted.

        :param text_formats: Ordered string replacement rules for the group labels.
        :type text_formats: [HeatgridTextFormatRule], optional

        :param width: Width of the label column.
        :type width: HeatgridLabelColumnWidth, optional
        """
        if text_formats is not unset:
            kwargs["text_formats"] = text_formats
        if width is not unset:
            kwargs["width"] = width
        super().__init__(kwargs)
