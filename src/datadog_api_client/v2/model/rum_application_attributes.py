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


class RUMApplicationAttributes(ModelNormal):
    validations = {
        "org_id": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "application_id": (str,),
            "created_at": (int,),
            "created_by_handle": (str,),
            "hash": (str,),
            "name": (str,),
            "org_id": (int,),
            "type": (str,),
            "updated_at": (int,),
            "updated_by_handle": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "created_at": "created_at",
        "created_by_handle": "created_by_handle",
        "hash": "hash",
        "name": "name",
        "org_id": "org_id",
        "type": "type",
        "updated_at": "updated_at",
        "updated_by_handle": "updated_by_handle",
    }

    def __init__(
        self_,
        application_id: str,
        created_at: int,
        created_by_handle: str,
        name: str,
        org_id: int,
        type: str,
        updated_at: int,
        updated_by_handle: str,
        hash: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        RUM application attributes.

        :param application_id: ID of the RUM application.
        :type application_id: str

        :param created_at: Timestamp in ms of the creation date.
        :type created_at: int

        :param created_by_handle: Handle of the creator user.
        :type created_by_handle: str

        :param hash: Client token of the RUM application.
        :type hash: str, optional

        :param name: Name of the RUM application.
        :type name: str

        :param org_id: Org ID of the RUM application.
        :type org_id: int

        :param type: Type of the RUM application. Supported values are ``browser`` , ``ios`` , ``android`` , ``react-native`` , ``flutter``.
        :type type: str

        :param updated_at: Timestamp in ms of the last update date.
        :type updated_at: int

        :param updated_by_handle: Handle of the updater user.
        :type updated_by_handle: str
        """
        if hash is not unset:
            kwargs["hash"] = hash
        super().__init__(kwargs)

        self_.application_id = application_id
        self_.created_at = created_at
        self_.created_by_handle = created_by_handle
        self_.name = name
        self_.org_id = org_id
        self_.type = type
        self_.updated_at = updated_at
        self_.updated_by_handle = updated_by_handle
