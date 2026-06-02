# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class StatuspageUrlSettingCreateAttributes(ModelNormal):
    validations = {
        "custom_tags": {
            "min_length": 1,
        },
        "url": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "custom_tags": (str,),
            "url": (str,),
        }

    attribute_map = {
        "custom_tags": "custom_tags",
        "url": "url",
    }

    def __init__(self_, custom_tags: str, url: str, **kwargs):
        """
        The Statuspage URL setting attributes for a create request.

        :param custom_tags: Comma-separated list of custom tags to apply to events generated from this Statuspage URL.
        :type custom_tags: str

        :param url: The Statuspage URL to monitor. Must be a ``status.io`` or ``statuspage.com`` URL.
        :type url: str
        """
        super().__init__(kwargs)

        self_.custom_tags = custom_tags
        self_.url = url
