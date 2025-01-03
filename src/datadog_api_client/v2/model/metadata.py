# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class Metadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "token": (str,),
            "total": (int,),
        }

    attribute_map = {
        "count": "count",
        "token": "token",
        "total": "total",
    }

    def __init__(self_, count: int, token: str, total: int, **kwargs):
        """
        The metadata related to this request.

        :param count: Number of entities included in the response.
        :type count: int

        :param token: The token that identifies the request.
        :type token: str

        :param total: Total number of entities across all pages.
        :type total: int
        """
        super().__init__(kwargs)

        self_.count = count
        self_.token = token
        self_.total = total
