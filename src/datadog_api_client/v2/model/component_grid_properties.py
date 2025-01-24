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
    from datadog_api_client.v2.model.component import Component
    from datadog_api_client.v2.model.component_grid_properties_is_visible import ComponentGridPropertiesIsVisible


class ComponentGridProperties(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.component import Component
        from datadog_api_client.v2.model.component_grid_properties_is_visible import ComponentGridPropertiesIsVisible

        return {
            "background_color": (str,),
            "children": ([Component],),
            "is_visible": (ComponentGridPropertiesIsVisible,),
        }

    attribute_map = {
        "background_color": "backgroundColor",
        "children": "children",
        "is_visible": "isVisible",
    }

    def __init__(
        self_,
        background_color: Union[str, UnsetType] = unset,
        children: Union[List[Component], UnsetType] = unset,
        is_visible: Union[ComponentGridPropertiesIsVisible, str, bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Properties of a grid component.

        :param background_color: The background color of the grid.
        :type background_color: str, optional

        :param children: The child components of the grid.
        :type children: [Component], optional

        :param is_visible: Whether the grid component and its children are visible. If a string, it must be a valid JavaScript expression that evaluates to a boolean.
        :type is_visible: ComponentGridPropertiesIsVisible, optional
        """
        if background_color is not unset:
            kwargs["background_color"] = background_color
        if children is not unset:
            kwargs["children"] = children
        if is_visible is not unset:
            kwargs["is_visible"] = is_visible
        super().__init__(kwargs)
