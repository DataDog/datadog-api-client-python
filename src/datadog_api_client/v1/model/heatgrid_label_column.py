# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.heatgrid_label_column_width import HeatgridLabelColumnWidth


class HeatgridLabelColumn(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_label_column_width import HeatgridLabelColumnWidth

        return {
            "width": (HeatgridLabelColumnWidth,),
        }

    attribute_map = {
        "width": "width",
    }

    def __init__(self_, width: HeatgridLabelColumnWidth, **kwargs):
        """
        Configuration of the group label column.

        :param width: Width of the label column.
        :type width: HeatgridLabelColumnWidth
        """
        super().__init__(kwargs)

        self_.width = width
