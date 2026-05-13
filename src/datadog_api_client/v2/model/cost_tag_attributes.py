# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CostTagAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "sources": ([str],),
            "value": (str,),
        }

    attribute_map = {
        "sources": "sources",
        "value": "value",
    }

    def __init__(self_, sources: List[str], value: str, **kwargs):
        """
        Attributes of a Cloud Cost Management tag.

        :param sources: List of sources that define this tag.
        :type sources: [str]

        :param value: The tag value in ``key:value`` format.
        :type value: str
        """
        super().__init__(kwargs)

        self_.sources = sources
        self_.value = value
