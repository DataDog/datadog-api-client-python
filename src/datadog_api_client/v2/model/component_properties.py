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
    from datadog_api_client.v2.model.component_properties_is_visible import ComponentPropertiesIsVisible


class ComponentProperties(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.component import Component
        from datadog_api_client.v2.model.component_properties_is_visible import ComponentPropertiesIsVisible

        return {
            "children": ([Component],),
            "is_visible": (ComponentPropertiesIsVisible,),
        }

    attribute_map = {
        "children": "children",
        "is_visible": "isVisible",
    }

    def __init__(
        self_,
        children: Union[List[Component], UnsetType] = unset,
        is_visible: Union[ComponentPropertiesIsVisible, bool, str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Properties of a UI component. Different component types can have their own additional unique properties. See the `components documentation <https://docs.datadoghq.com/service_management/app_builder/components/>`_ for more detail on each component type and its properties.

        :param children: The child components of the UI component.
        :type children: [Component], optional

        :param is_visible: Whether the UI component is visible. If this is a string, it must be a valid JavaScript expression that evaluates to a boolean.
        :type is_visible: ComponentPropertiesIsVisible, optional
        """
        if children is not unset:
            kwargs["children"] = children
        if is_visible is not unset:
            kwargs["is_visible"] = is_visible
        super().__init__(kwargs)
