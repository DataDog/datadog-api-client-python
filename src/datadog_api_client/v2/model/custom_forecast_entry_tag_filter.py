# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CustomForecastEntryTagFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "tag_key": (str,),
            "tag_value": (str,),
        }

    attribute_map = {
        "tag_key": "tag_key",
        "tag_value": "tag_value",
    }

    def __init__(self_, tag_key: str, tag_value: str, **kwargs):
        """
        A tag filter that scopes a custom forecast entry to specific resource tags.

        :param tag_key: The tag key to filter on.
        :type tag_key: str

        :param tag_value: The tag value to filter on.
        :type tag_value: str
        """
        super().__init__(kwargs)

        self_.tag_key = tag_key
        self_.tag_value = tag_value
