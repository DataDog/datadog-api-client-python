# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CostTagKeyDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "tag_values": ([str],),
        }

    attribute_map = {
        "description": "description",
        "tag_values": "tag_values",
    }

    def __init__(self_, description: str, tag_values: List[str], **kwargs):
        """
        Additional details for a Cloud Cost Management tag key, including its description and example tag values.

        :param description: Description of the tag key.
        :type description: str

        :param tag_values: Example tag values observed for this tag key.
        :type tag_values: [str]
        """
        super().__init__(kwargs)

        self_.description = description
        self_.tag_values = tag_values
