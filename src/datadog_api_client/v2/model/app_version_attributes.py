# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
    UUID,
)


class AppVersionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "app_id": (UUID,),
            "created_at": (datetime,),
            "has_ever_been_published": (bool,),
            "name": (str,),
            "updated_at": (datetime,),
            "user_id": (int,),
            "user_name": (str,),
            "user_uuid": (UUID,),
            "version": (int,),
        }

    attribute_map = {
        "app_id": "app_id",
        "created_at": "created_at",
        "has_ever_been_published": "has_ever_been_published",
        "name": "name",
        "updated_at": "updated_at",
        "user_id": "user_id",
        "user_name": "user_name",
        "user_uuid": "user_uuid",
        "version": "version",
    }

    def __init__(
        self_,
        app_id: Union[UUID, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        has_ever_been_published: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        user_id: Union[int, UnsetType] = unset,
        user_name: Union[str, UnsetType] = unset,
        user_uuid: Union[UUID, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes describing an app version.

        :param app_id: The ID of the app this version belongs to.
        :type app_id: UUID, optional

        :param created_at: Timestamp of when the version was created.
        :type created_at: datetime, optional

        :param has_ever_been_published: Whether this version has ever been published.
        :type has_ever_been_published: bool, optional

        :param name: The optional human-readable name of the version.
        :type name: str, optional

        :param updated_at: Timestamp of when the version was last updated.
        :type updated_at: datetime, optional

        :param user_id: The ID of the user who created the version.
        :type user_id: int, optional

        :param user_name: The name (or email) of the user who created the version.
        :type user_name: str, optional

        :param user_uuid: The UUID of the user who created the version.
        :type user_uuid: UUID, optional

        :param version: The version number of the app, starting at 1.
        :type version: int, optional
        """
        if app_id is not unset:
            kwargs["app_id"] = app_id
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if has_ever_been_published is not unset:
            kwargs["has_ever_been_published"] = has_ever_been_published
        if name is not unset:
            kwargs["name"] = name
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if user_id is not unset:
            kwargs["user_id"] = user_id
        if user_name is not unset:
            kwargs["user_name"] = user_name
        if user_uuid is not unset:
            kwargs["user_uuid"] = user_uuid
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
