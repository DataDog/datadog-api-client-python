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


class ClientTokenUpdateRequest(ModelNormal):
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
            "hash": (str,),
            "name": (str,),
            "origin_urls": ([str],),
        }

    attribute_map = {
        "hash": "hash",
        "name": "name",
        "origin_urls": "origin_urls",
    }

    def __init__(self_, hash: str, name: str, origin_urls: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Request to update an existing client token.

        :param hash: Hash value of the client token to update.
        :type hash: str

        :param name: New name for the client token.
        :type name: str

        :param origin_urls: New list of allowed origin URLs. If provided, this will replace the existing list.
        :type origin_urls: [str], optional
        """
        if origin_urls is not unset:
            kwargs["origin_urls"] = origin_urls
        super().__init__(kwargs)

        self_.hash = hash
        self_.name = name
