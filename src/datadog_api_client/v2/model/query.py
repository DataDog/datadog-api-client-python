# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.app_builder_event import AppBuilderEvent
    from datadog_api_client.v2.model.query_type import QueryType


class Query(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_builder_event import AppBuilderEvent
        from datadog_api_client.v2.model.query_type import QueryType

        return {
            "events": ([AppBuilderEvent],),
            "id": (UUID,),
            "name": (str,),
            "properties": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "type": (QueryType,),
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
        type: QueryType,
        events: Union[List[AppBuilderEvent], UnsetType] = unset,
        properties: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        A query used by an app. This can take the form of an external action, a data transformation, or a state variable change.

        :param events: Events to listen for downstream of the query.
        :type events: [AppBuilderEvent], optional

        :param id: The ID of the query.
        :type id: UUID

        :param name: The name of the query. The name must be unique within the app and is visible in the app editor.
        :type name: str

        :param properties: The properties of the query. The properties vary depending on the query type.
        :type properties: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param type: The query type.
        :type type: QueryType
        """
        if events is not unset:
            kwargs["events"] = events
        if properties is not unset:
            kwargs["properties"] = properties
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
        self_.type = type
