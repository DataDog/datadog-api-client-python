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
    validations = {
        "name": {
            "max_length": 256,
            "min_length": 1,
        },
        "scopes": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "expires_at": (datetime,),
            "modified_at": (datetime, none_type),
            "name": (str,),
            "scopes": ([str],),
        }

    attribute_map = {
        "created_at": "created_at",
        "expires_at": "expires_at",
        "modified_at": "modified_at",
        "name": "name",
        "scopes": "scopes",
    }
    read_only_vars = {
        "created_at",
        "modified_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        expires_at: datetime,
        name: str,
        scopes: List[str],
        modified_at: Union[datetime, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a personal access token.

        :param created_at: Creation timestamp of the personal access token.
        :type created_at: datetime

        :param expires_at: Expiration timestamp of the personal access token.
        :type expires_at: datetime

        :param modified_at: Last modification timestamp of the personal access token.
        :type modified_at: datetime, none_type, optional

        :param name: Name of the personal access token.
        :type name: str

        :param scopes: Array of scopes granted to the personal access token. These define what
            permissions the token has.
        :type scopes: [str]
        """
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.expires_at = expires_at
        self_.name = name
        self_.scopes = scopes
