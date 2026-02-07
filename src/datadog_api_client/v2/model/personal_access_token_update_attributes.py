# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class PersonalAccessTokenUpdateAttributes(ModelNormal):
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
            "name": (str,),
            "scopes": ([str],),
        }

    attribute_map = {
        "name": "name",
        "scopes": "scopes",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, scopes: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Attributes used to update a personal access token.

        :param name: New name for the personal access token.
        :type name: str, optional

        :param scopes: New array of scopes for the personal access token. If provided, this will
            replace the existing scopes.
        :type scopes: [str], optional
        """
        if name is not unset:
            kwargs["name"] = name
        if scopes is not unset:
            kwargs["scopes"] = scopes
        super().__init__(kwargs)
