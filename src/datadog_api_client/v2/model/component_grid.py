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
    from datadog_api_client.v2.model.app_builder_event import AppBuilderEvent
    from datadog_api_client.v2.model.component_grid_properties import ComponentGridProperties
    from datadog_api_client.v2.model.component_grid_type import ComponentGridType


class ComponentGrid(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_builder_event import AppBuilderEvent
        from datadog_api_client.v2.model.component_grid_properties import ComponentGridProperties
        from datadog_api_client.v2.model.component_grid_type import ComponentGridType

        return {
            "events": ([AppBuilderEvent],),
            "id": (str,),
            "name": (str,),
            "properties": (ComponentGridProperties,),
            "type": (ComponentGridType,),
        }

    attribute_map = {
        "events": "events",
        "id": "id",
        "name": "name",
        "properties": "properties",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        properties: ComponentGridProperties,
        type: ComponentGridType,
        events: Union[List[AppBuilderEvent], UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A grid component. The grid component is the root canvas for an app and contains all other components.

        :param events: Events to listen for on the grid component.
        :type events: [AppBuilderEvent], optional

        :param id: The ID of the grid component. This property is deprecated; use ``name`` to identify individual components instead.
        :type id: str, optional

        :param name: A unique identifier for this grid component. This name is also visible in the app editor.
        :type name: str

        :param properties: Properties of a grid component.
        :type properties: ComponentGridProperties

        :param type: The grid component type.
        :type type: ComponentGridType
        """
        if events is not unset:
            kwargs["events"] = events
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.name = name
        self_.properties = properties
        self_.type = type
