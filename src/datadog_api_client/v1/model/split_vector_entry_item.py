# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SplitVectorEntryItem(ModelNormal):
    validations = {
        "tag_key": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "tag_key": (str,),
            "tag_values": ([str],),
        }

    attribute_map = {
        "tag_key": "tag_key",
        "tag_values": "tag_values",
    }

    def __init__(self_, tag_key: str, tag_values: List[str], **kwargs):
        """
        The split graph list contains a graph for each value of the split dimension.

        :param tag_key: The tag key.
        :type tag_key: str

        :param tag_values: The tag values.
        :type tag_values: [str]
        """
        super().__init__(kwargs)

        self_.tag_key = tag_key
        self_.tag_values = tag_values
