# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GoogleChatTargetAudienceAttributes(ModelNormal):
    validations = {
        "audience_id": {
            "max_length": 255,
        },
        "audience_name": {
            "max_length": 255,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "audience_id": (str,),
            "audience_name": (str,),
        }

    attribute_map = {
        "audience_id": "audience_id",
        "audience_name": "audience_name",
    }

    def __init__(self_, audience_id: str, audience_name: str, **kwargs):
        """
        Google Chat target audience attributes.

        :param audience_id: The audience ID.
        :type audience_id: str

        :param audience_name: The audience name.
        :type audience_name: str
        """
        super().__init__(kwargs)

        self_.audience_id = audience_id
        self_.audience_name = audience_name
