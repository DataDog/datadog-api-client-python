# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class Event(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "integration_id": (str,),
            "name": (str,),
            "source_id": (int,),
            "type": (str,),
            "uid": (str,),
        }

    attribute_map = {
        "id": "id",
        "integration_id": "integration_id",
        "name": "name",
        "source_id": "source_id",
        "type": "type",
        "uid": "uid",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        integration_id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        source_id: Union[int, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        uid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The metadata associated with a request.

        :param id: Event ID.
        :type id: str, optional

        :param integration_id: The integration ID of the event.
        :type integration_id: str, optional

        :param name: The event name.
        :type name: str, optional

        :param source_id: Event source ID.
        :type source_id: int, optional

        :param type: Event type.
        :type type: str, optional

        :param uid: A unique identifier for the event. You can use this identifier to query or reference the event.
        :type uid: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if integration_id is not unset:
            kwargs["integration_id"] = integration_id
        if name is not unset:
            kwargs["name"] = name
        if source_id is not unset:
            kwargs["source_id"] = source_id
        if type is not unset:
            kwargs["type"] = type
        if uid is not unset:
            kwargs["uid"] = uid
        super().__init__(kwargs)
