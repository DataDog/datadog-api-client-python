# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GeneratedCostTagDescriptionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
        }

    attribute_map = {
        "description": "description",
    }

    def __init__(self_, description: str, **kwargs):
        """
        Attributes of an AI-generated Cloud Cost Management tag key description.

        :param description: The AI-generated description for the tag key.
        :type description: str
        """
        super().__init__(kwargs)

        self_.description = description
