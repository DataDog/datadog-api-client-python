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
    from datadog_api_client.v1_20270101.model.tree_data_projection_treemap_dimensions_items_dimension import (
        TreeDataProjectionTreemapDimensionsItemsDimension,
    )
    from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat


class TreeDataProjectionTreemapDimensionsItems(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.tree_data_projection_treemap_dimensions_items_dimension import (
            TreeDataProjectionTreemapDimensionsItemsDimension,
        )
        from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat

        return {
            "column": (str,),
            "dimension": (TreeDataProjectionTreemapDimensionsItemsDimension,),
            "number_format": (WidgetNumberFormat,),
        }

    attribute_map = {
        "column": "column",
        "dimension": "dimension",
        "number_format": "number_format",
    }

    def __init__(
        self_,
        column: str,
        dimension: TreeDataProjectionTreemapDimensionsItemsDimension,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param dimension: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimension: TreeDataProjectionTreemapDimensionsItemsDimension

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional
        """
        if number_format is not unset:
            kwargs["number_format"] = number_format
        super().__init__(kwargs)

        self_.column = column
        self_.dimension = dimension
