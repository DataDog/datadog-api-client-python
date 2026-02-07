# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class ClientToken(ModelNormal):
    validations = {
        "hash": {
            "max_length": 35,
        },
        "name": {
            "max_length": 255,
            "min_length": 1,
        },
        "origin_urls": {
            "max_items": 100,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "created_by_handle": (str,),
            "created_by_uuid": (UUID,),
            "disabled_at": (datetime, none_type),
            "disabled_by": (int,),
            "disabled_by_handle": (str,),
            "hash": (str,),
            "modified_by": (int,),
            "name": (str,),
            "org_id": (int,),
            "origin_urls": ([str],),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by_handle": "created_by_handle",
        "created_by_uuid": "created_by_uuid",
        "disabled_at": "disabled_at",
        "disabled_by": "disabled_by",
        "disabled_by_handle": "disabled_by_handle",
        "hash": "hash",
        "modified_by": "modified_by",
        "name": "name",
        "org_id": "org_id",
        "origin_urls": "origin_urls",
    }
    read_only_vars = {
        "created_at",
        "created_by_handle",
        "created_by_uuid",
        "disabled_at",
        "disabled_by",
        "disabled_by_handle",
        "hash",
        "modified_by",
        "org_id",
    }

    def __init__(
        self_,
        origin_urls: List[str],
        created_at: Union[datetime, UnsetType] = unset,
        created_by_handle: Union[str, UnsetType] = unset,
        created_by_uuid: Union[UUID, UnsetType] = unset,
        disabled_at: Union[datetime, none_type, UnsetType] = unset,
        disabled_by: Union[int, UnsetType] = unset,
        disabled_by_handle: Union[str, UnsetType] = unset,
        hash: Union[str, UnsetType] = unset,
        modified_by: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Client token object. Client tokens (also known as public API keys) enable you to submit
        data from your browser or mobile applications to Datadog.

        :param created_at: Creation timestamp of the client token.
        :type created_at: datetime, optional

        :param created_by_handle: Handle of the user who created the client token.
        :type created_by_handle: str, optional

        :param created_by_uuid: UUID of the user who created the client token.
        :type created_by_uuid: UUID, optional

        :param disabled_at: Timestamp when the client token was disabled.
        :type disabled_at: datetime, none_type, optional

        :param disabled_by: ID of the user who disabled the client token.
        :type disabled_by: int, optional

        :param disabled_by_handle: Handle of the user who disabled the client token.
        :type disabled_by_handle: str, optional

        :param hash: The hash value of the client token. This is the secret token value that should be
            used in your browser or mobile application.
        :type hash: str, optional

        :param modified_by: ID of the user who last modified the client token.
        :type modified_by: int, optional

        :param name: Name of the client token.
        :type name: str, optional

        :param org_id: Organization ID associated with the client token.
        :type org_id: int, optional

        :param origin_urls: List of allowed origin URLs for browser-based applications. Requests from URLs
            not in this list will be rejected.
        :type origin_urls: [str]
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by_handle is not unset:
            kwargs["created_by_handle"] = created_by_handle
        if created_by_uuid is not unset:
            kwargs["created_by_uuid"] = created_by_uuid
        if disabled_at is not unset:
            kwargs["disabled_at"] = disabled_at
        if disabled_by is not unset:
            kwargs["disabled_by"] = disabled_by
        if disabled_by_handle is not unset:
            kwargs["disabled_by_handle"] = disabled_by_handle
        if hash is not unset:
            kwargs["hash"] = hash
        if modified_by is not unset:
            kwargs["modified_by"] = modified_by
        if name is not unset:
            kwargs["name"] = name
        if org_id is not unset:
            kwargs["org_id"] = org_id
        super().__init__(kwargs)

        self_.origin_urls = origin_urls
