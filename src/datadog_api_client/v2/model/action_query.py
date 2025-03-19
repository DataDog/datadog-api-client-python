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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.app_builder_event import AppBuilderEvent
    from datadog_api_client.v2.model.action_query_properties import ActionQueryProperties
    from datadog_api_client.v2.model.action_query_type import ActionQueryType


class ActionQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_builder_event import AppBuilderEvent
        from datadog_api_client.v2.model.action_query_properties import ActionQueryProperties
        from datadog_api_client.v2.model.action_query_type import ActionQueryType

        return {
            "events": ([AppBuilderEvent],),
            "id": (UUID,),
            "name": (str,),
            "properties": (ActionQueryProperties,),
            "type": (ActionQueryType,),
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
        id: UUID,
        name: str,
        properties: ActionQueryProperties,
        type: ActionQueryType,
        events: Union[List[AppBuilderEvent], UnsetType] = unset,
        **kwargs,
    ):
        """
        An action query. This query type is used to trigger an action, such as sending a HTTP request.

        :param events: Events to listen for downstream of the action query.
        :type events: [AppBuilderEvent], optional

        :param id: The ID of the action query.
        :type id: UUID

        :param name: A unique identifier for this action query. This name is also used to access the query's result throughout the app.
        :type name: str

        :param properties: The properties of the action query.
        :type properties: ActionQueryProperties

        :param type: The action query type.
        :type type: ActionQueryType
        """
        if events is not unset:
            kwargs["events"] = events
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
        self_.properties = properties
        self_.type = type
