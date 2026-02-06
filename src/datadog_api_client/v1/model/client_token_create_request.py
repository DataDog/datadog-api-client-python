# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ClientTokenCreateRequest(ModelNormal):
    validations = {
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
            "name": (str,),
            "origin_urls": ([str],),
        }

    attribute_map = {
        "name": "name",
        "origin_urls": "origin_urls",
    }

    def __init__(self_, name: str, origin_urls: List[str], **kwargs):
        """
        Request to create a new client token.

        :param name: Name of the client token.
        :type name: str

        :param origin_urls: List of allowed origin URLs for browser-based applications. Requests from URLs
            not in this list will be rejected.
        :type origin_urls: [str]
        """
        super().__init__(kwargs)

        self_.name = name
        self_.origin_urls = origin_urls
