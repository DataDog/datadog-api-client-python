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
)


class PersonalAccessTokenAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "expires_at": (datetime, none_type),
            "last_used_at": (datetime, none_type),
            "modified_at": (datetime, none_type),
            "name": (str,),
            "public_portion": (str,),
            "scopes": ([str],),
        }

    attribute_map = {
        "created_at": "created_at",
        "expires_at": "expires_at",
        "last_used_at": "last_used_at",
        "modified_at": "modified_at",
        "name": "name",
        "public_portion": "public_portion",
        "scopes": "scopes",
    }
    read_only_vars = {
        "created_at",
        "expires_at",
        "last_used_at",
        "modified_at",
        "public_portion",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        expires_at: Union[datetime, none_type, UnsetType] = unset,
        last_used_at: Union[datetime, none_type, UnsetType] = unset,
        modified_at: Union[datetime, none_type, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        public_portion: Union[str, UnsetType] = unset,
        scopes: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a personal access token.

        :param created_at: Creation date of the personal access token.
        :type created_at: datetime, optional

        :param expires_at: Expiration date of the personal access token.
        :type expires_at: datetime, none_type, optional

        :param last_used_at: Date the personal access token was last used.
        :type last_used_at: datetime, none_type, optional

        :param modified_at: Date of last modification of the personal access token.
        :type modified_at: datetime, none_type, optional

        :param name: Name of the personal access token.
        :type name: str, optional

        :param public_portion: The public portion of the personal access token.
        :type public_portion: str, optional

        :param scopes: Array of scopes granted to the personal access token.
        :type scopes: [str], optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if expires_at is not unset:
            kwargs["expires_at"] = expires_at
        if last_used_at is not unset:
            kwargs["last_used_at"] = last_used_at
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if name is not unset:
            kwargs["name"] = name
        if public_portion is not unset:
            kwargs["public_portion"] = public_portion
        if scopes is not unset:
            kwargs["scopes"] = scopes
        super().__init__(kwargs)
