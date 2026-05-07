# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CostAIPreferredTagsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "message": (str,),
            "preferred_tags": ([str],),
        }

    attribute_map = {
        "message": "message",
        "preferred_tags": "preferred_tags",
    }

    def __init__(self_, message: str, preferred_tags: List[str], **kwargs):
        """
        Attributes for the preferred tags response.

        :param message: A contextual message about the preferred tags configuration.
        :type message: str

        :param preferred_tags: The list of preferred cost allocation tags.
        :type preferred_tags: [str]
        """
        super().__init__(kwargs)

        self_.message = message
        self_.preferred_tags = preferred_tags
