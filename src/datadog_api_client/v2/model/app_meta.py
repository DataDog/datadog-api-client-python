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


class AppMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (str,),
            "deleted_at": (str,),
            "org_id": (int,),
            "run_as_user": (str,),
            "updated_at": (str,),
            "updated_since_deployment": (bool,),
            "user_id": (int,),
            "user_name": (str,),
            "user_uuid": (str,),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "deleted_at": "deleted_at",
        "org_id": "org_id",
        "run_as_user": "run_as_user",
        "updated_at": "updated_at",
        "updated_since_deployment": "updated_since_deployment",
        "user_id": "user_id",
        "user_name": "user_name",
        "user_uuid": "user_uuid",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: Union[str, UnsetType] = unset,
        deleted_at: Union[str, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        run_as_user: Union[str, UnsetType] = unset,
        updated_at: Union[str, UnsetType] = unset,
        updated_since_deployment: Union[bool, UnsetType] = unset,
        user_id: Union[int, UnsetType] = unset,
        user_name: Union[str, UnsetType] = unset,
        user_uuid: Union[str, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``AppMeta`` object.

        :param created_at: The ``AppMeta`` ``created_at``.
        :type created_at: str, optional

        :param deleted_at: The ``AppMeta`` ``deleted_at``.
        :type deleted_at: str, optional

        :param org_id: The ``AppMeta`` ``org_id``.
        :type org_id: int, optional

        :param run_as_user: The ``AppMeta`` ``run_as_user``.
        :type run_as_user: str, optional

        :param updated_at: The ``AppMeta`` ``updated_at``.
        :type updated_at: str, optional

        :param updated_since_deployment: The ``AppMeta`` ``updated_since_deployment``.
        :type updated_since_deployment: bool, optional

        :param user_id: The ``AppMeta`` ``user_id``.
        :type user_id: int, optional

        :param user_name: The ``AppMeta`` ``user_name``.
        :type user_name: str, optional

        :param user_uuid: The ``AppMeta`` ``user_uuid``.
        :type user_uuid: str, optional

        :param version: The ``AppMeta`` ``version``.
        :type version: int, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if run_as_user is not unset:
            kwargs["run_as_user"] = run_as_user
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
