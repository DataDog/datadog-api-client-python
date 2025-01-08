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


class DeploymentRelationshipMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (str,),
            "user_id": (int,),
            "user_name": (str,),
            "user_uuid": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "user_id": "user_id",
        "user_name": "user_name",
        "user_uuid": "user_uuid",
    }

    def __init__(
        self_,
        created_at: Union[str, UnsetType] = unset,
        user_id: Union[int, UnsetType] = unset,
        user_name: Union[str, UnsetType] = unset,
        user_uuid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``DeploymentRelationshipMeta`` object.

        :param created_at: The ``meta`` ``created_at``.
        :type created_at: str, optional

        :param user_id: The ``meta`` ``user_id``.
        :type user_id: int, optional

        :param user_name: The ``meta`` ``user_name``.
        :type user_name: str, optional

        :param user_uuid: The ``meta`` ``user_uuid``.
        :type user_uuid: str, optional
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
