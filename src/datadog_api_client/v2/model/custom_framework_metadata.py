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


class CustomFrameworkMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (int,),
            "created_by": (str,),
            "description": (str,),
            "handle": (str,),
            "icon_url": (str,),
            "id": (str,),
            "name": (str,),
            "org_id": (int,),
            "updated_at": (int,),
            "version": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "description": "description",
        "handle": "handle",
        "icon_url": "icon_url",
        "id": "id",
        "name": "name",
        "org_id": "org_id",
        "updated_at": "updated_at",
        "version": "version",
    }

    def __init__(
        self_,
        handle: str,
        id: str,
        name: str,
        org_id: int,
        version: str,
        created_at: Union[int, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        icon_url: Union[str, UnsetType] = unset,
        updated_at: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object for an organization's custom frameworks.

        :param created_at: Framework Creation Date
        :type created_at: int, optional

        :param created_by: Framework Creator
        :type created_by: str, optional

        :param description: Framework Description
        :type description: str, optional

        :param handle: Framework Handle
        :type handle: str

        :param icon_url: Framework Icon URL
        :type icon_url: str, optional

        :param id: Custom Framework ID
        :type id: str

        :param name: Framework Name
        :type name: str

        :param org_id: Org ID
        :type org_id: int

        :param updated_at: Framework Update Date
        :type updated_at: int, optional

        :param version: Framework Version
        :type version: str
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if description is not unset:
            kwargs["description"] = description
        if icon_url is not unset:
            kwargs["icon_url"] = icon_url
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.handle = handle
        self_.id = id
        self_.name = name
        self_.org_id = org_id
        self_.version = version
