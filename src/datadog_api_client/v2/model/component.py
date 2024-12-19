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
        The definition of ``Component`` object.

        :param events: The ``Component`` ``events``.
        :type events: [AppBuilderEvent], optional

        :param id: The ``Component`` ``id``.
        :type id: str, none_type, optional

        :param name: The ``Component`` ``name``.
        :type name: str

        :param properties: The definition of ``ComponentProperties`` object.
        :type properties: ComponentProperties

        :param type: The definition of ``ComponentType`` object.
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
