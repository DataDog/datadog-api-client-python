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


class AppMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "deleted_at": (datetime,),
            "org_id": (int,),
            "updated_at": (datetime,),
            "updated_since_deployment": (bool,),
            "user_id": (int,),
            "user_name": (str,),
            "user_uuid": (UUID,),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "deleted_at": "deleted_at",
        "org_id": "org_id",
        "updated_at": "updated_at",
        "updated_since_deployment": "updated_since_deployment",
        "user_id": "user_id",
        "user_name": "user_name",
        "user_uuid": "user_uuid",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        deleted_at: Union[datetime, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        updated_since_deployment: Union[bool, UnsetType] = unset,
        user_id: Union[int, UnsetType] = unset,
        user_name: Union[str, UnsetType] = unset,
        user_uuid: Union[UUID, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata of an app.

        :param created_at: Timestamp of when the app was created.
        :type created_at: datetime, optional

        :param deleted_at: Timestamp of when the app was deleted.
        :type deleted_at: datetime, optional

        :param org_id: The Datadog organization ID that owns the app.
        :type org_id: int, optional

        :param updated_at: Timestamp of when the app was last updated.
        :type updated_at: datetime, optional

        :param updated_since_deployment: Whether the app was updated since it was last published. Published apps are pinned to a specific version and do not automatically update when the app is updated.
        :type updated_since_deployment: bool, optional

        :param user_id: The ID of the user who created the app.
        :type user_id: int, optional

        :param user_name: The name (or email address) of the user who created the app.
        :type user_name: str, optional

        :param user_uuid: The UUID of the user who created the app.
        :type user_uuid: UUID, optional

        :param version: The version number of the app. This starts at 1 and increments with each update.
        :type version: int, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_since_deployment is not unset:
            kwargs["updated_since_deployment"] = updated_since_deployment
        if user_id is not unset:
            kwargs["user_id"] = user_id
        if user_name is not unset:
            kwargs["user_name"] = user_name
        if user_uuid is not unset:
            kwargs["user_uuid"] = user_uuid
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
