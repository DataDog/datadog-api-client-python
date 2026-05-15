# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CostTagKeySourceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "tag_key": (str,),
            "tag_sources": ([str],),
        }

    attribute_map = {
        "tag_key": "tag_key",
        "tag_sources": "tag_sources",
    }

    def __init__(self_, tag_key: str, tag_sources: List[str], **kwargs):
        """
        Attributes of a Cloud Cost Management tag source.

        :param tag_key: The tag key name.
        :type tag_key: str

        :param tag_sources: Origins where this tag key was observed (for example, ``aws-user-defined`` ).
        :type tag_sources: [str]
        """
        super().__init__(kwargs)

        self_.tag_key = tag_key
        self_.tag_sources = tag_sources
