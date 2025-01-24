# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.app_builder_event import AppBuilderEvent
    from datadog_api_client.v2.model.component_properties import ComponentProperties
    from datadog_api_client.v2.model.component_type import ComponentType


class Component(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_builder_event import AppBuilderEvent
        from datadog_api_client.v2.model.component_properties import ComponentProperties
        from datadog_api_client.v2.model.component_type import ComponentType

        return {
            "events": ([AppBuilderEvent],),
            "id": (str, none_type),
            "name": (str,),
            "properties": (ComponentProperties,),
            "type": (ComponentType,),
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
        properties: ComponentProperties,
        type: ComponentType,
        events: Union[List[AppBuilderEvent], UnsetType] = unset,
        id: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        `Definition of a UI component in the app <https://docs.datadoghq.com/service_management/app_builder/components/>`_

        :param events: Events to listen for on the UI component.
        :type events: [AppBuilderEvent], optional

        :param id: The ID of the UI component. This property is deprecated; use ``name`` to identify individual components instead.
        :type id: str, none_type, optional

        :param name: A unique identifier for this UI component. This name is also visible in the app editor.
        :type name: str

        :param properties: Properties of a UI component. Different component types can have their own additional unique properties. See the `components documentation <https://docs.datadoghq.com/service_management/app_builder/components/>`_ for more detail on each component type and its properties.
        :type properties: ComponentProperties

        :param type: The UI component type.
        :type type: ComponentType
        """
        if events is not unset:
            kwargs["events"] = events
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.name = name
        self_.properties = properties
        self_.type = type
