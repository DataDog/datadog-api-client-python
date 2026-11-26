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
    from datadog_api_client.v1_20270101.model.tree_data_projection_sunburst_dimensions_items import (
        TreeDataProjectionSunburstDimensionsItems,
    )
    from datadog_api_client.v1_20270101.model.group_style_rule import GroupStyleRule
    from datadog_api_client.v1_20270101.model.tree_data_projection_sunburst_type import TreeDataProjectionSunburstType


class TreeDataProjectionSunburst(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.tree_data_projection_sunburst_dimensions_items import (
            TreeDataProjectionSunburstDimensionsItems,
        )
        from datadog_api_client.v1_20270101.model.group_style_rule import GroupStyleRule
        from datadog_api_client.v1_20270101.model.tree_data_projection_sunburst_type import (
            TreeDataProjectionSunburstType,
        )

        return {
            "dimensions": ([TreeDataProjectionSunburstDimensionsItems],),
            "group_styles": ([GroupStyleRule],),
            "type": (TreeDataProjectionSunburstType,),
        }

    attribute_map = {
        "dimensions": "dimensions",
        "group_styles": "group_styles",
        "type": "type",
    }

    def __init__(
        self_,
        dimensions: List[TreeDataProjectionSunburstDimensionsItems],
        type: TreeDataProjectionSunburstType,
        group_styles: Union[List[GroupStyleRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param dimensions: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimensions: [TreeDataProjectionSunburstDimensionsItems]

        :param group_styles: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_styles: [GroupStyleRule], optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: TreeDataProjectionSunburstType
        """
        if group_styles is not unset:
            kwargs["group_styles"] = group_styles
        super().__init__(kwargs)

        self_.dimensions = dimensions
        self_.type = type
