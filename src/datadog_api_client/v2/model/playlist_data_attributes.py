# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.playlist_data_attributes_created_by import PlaylistDataAttributesCreatedBy


class PlaylistDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.playlist_data_attributes_created_by import PlaylistDataAttributesCreatedBy

        return {
            "created_at": (datetime,),
            "created_by": (PlaylistDataAttributesCreatedBy,),
            "description": (str,),
            "name": (str,),
            "session_count": (int,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "description": "description",
        "name": "name",
        "session_count": "session_count",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        name: str,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[PlaylistDataAttributesCreatedBy, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        session_count: Union[int, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param created_at:
        :type created_at: datetime, optional

        :param created_by:
        :type created_by: PlaylistDataAttributesCreatedBy, optional

        :param description:
        :type description: str, optional

        :param name:
        :type name: str

        :param session_count:
        :type session_count: int, optional

        :param updated_at:
        :type updated_at: datetime, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if description is not unset:
            kwargs["description"] = description
        if session_count is not unset:
            kwargs["session_count"] = session_count
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.name = name
