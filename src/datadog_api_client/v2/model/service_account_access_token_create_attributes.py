# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class ServiceAccountAccessTokenCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "expires_at": (datetime,),
            "name": (str,),
            "scopes": ([str],),
        }

    attribute_map = {
        "expires_at": "expires_at",
        "name": "name",
        "scopes": "scopes",
    }

    def __init__(self_, name: str, scopes: List[str], expires_at: Union[datetime, UnsetType] = unset, **kwargs):
        """
        Attributes used to create a service account access token.

        :param expires_at: Expiration date of the access token. Optional for service account tokens.
        :type expires_at: datetime, optional

        :param name: Name of the access token.
        :type name: str

        :param scopes: Array of scopes to grant the access token.
        :type scopes: [str]
        """
        if expires_at is not unset:
            kwargs["expires_at"] = expires_at
        super().__init__(kwargs)

        self_.name = name
        self_.scopes = scopes
