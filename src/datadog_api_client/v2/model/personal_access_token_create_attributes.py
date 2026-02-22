# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class PersonalAccessTokenCreateAttributes(ModelNormal):
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
            "expires_at": (datetime,),
            "name": (str,),
            "scopes": ([str],),
        }

    attribute_map = {
        "expires_at": "expires_at",
        "name": "name",
        "scopes": "scopes",
    }

    def __init__(self_, expires_at: datetime, name: str, scopes: List[str], **kwargs):
        """
        Attributes used to create a personal access token.

        :param expires_at: Expiration timestamp for the personal access token.
        :type expires_at: datetime

        :param name: Name of the personal access token.
        :type name: str

        :param scopes: Array of scopes to grant the personal access token. These define what
            permissions the token will have.
        :type scopes: [str]
        """
        super().__init__(kwargs)

        self_.expires_at = expires_at
        self_.name = name
        self_.scopes = scopes
