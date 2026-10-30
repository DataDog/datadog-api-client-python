# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AIGuardRedactionReplacement(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "path": (str,),
            "replacement": (str,),
        }

    attribute_map = {
        "path": "path",
        "replacement": "replacement",
    }

    def __init__(self_, path: str, replacement: str, **kwargs):
        """
        The fully redacted content for one path in the request.

        :param path: The path of the redacted content relative to the request attributes.
        :type path: str

        :param replacement: The redacted replacement content.
        :type replacement: str
        """
        super().__init__(kwargs)

        self_.path = path
        self_.replacement = replacement
