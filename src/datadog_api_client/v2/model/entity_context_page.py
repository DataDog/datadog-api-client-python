# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class EntityContextPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next_token": (str,),
        }

    attribute_map = {
        "next_token": "next_token",
    }

    def __init__(self_, next_token: str, **kwargs):
        """
        Pagination metadata for the entity context response.

        :param next_token: An opaque token to pass as ``page_token`` in a subsequent request to retrieve the next page of results. Empty when there are no more results.
        :type next_token: str
        """
        super().__init__(kwargs)

        self_.next_token = next_token
