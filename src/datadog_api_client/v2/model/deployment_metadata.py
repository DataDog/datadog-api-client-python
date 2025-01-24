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


class DeploymentMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "user_id": (int,),
            "user_name": (str,),
            "user_uuid": (UUID,),
        }

    attribute_map = {
        "created_at": "created_at",
        "user_id": "user_id",
        "user_name": "user_name",
        "user_uuid": "user_uuid",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        user_id: Union[int, UnsetType] = unset,
        user_name: Union[str, UnsetType] = unset,
        user_uuid: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata object containing the publication creation information.

        :param created_at: Timestamp of when the app was published.
        :type created_at: datetime, optional

        :param user_id: The ID of the user who published the app.
        :type user_id: int, optional

        :param user_name: The name (or email address) of the user who published the app.
        :type user_name: str, optional

        :param user_uuid: The UUID of the user who published the app.
        :type user_uuid: UUID, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if user_id is not unset:
            kwargs["user_id"] = user_id
        if user_name is not unset:
            kwargs["user_name"] = user_name
        if user_uuid is not unset:
            kwargs["user_uuid"] = user_uuid
        super().__init__(kwargs)
