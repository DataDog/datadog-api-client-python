# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentStatuspagePreferencesDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "subscribed": (bool,),
        }

    attribute_map = {
        "subscribed": "subscribed",
    }

    def __init__(self_, subscribed: bool, **kwargs):
        """
        Attributes of subscription preferences.

        :param subscribed: Whether the user is subscribed.
        :type subscribed: bool
        """
        super().__init__(kwargs)

        self_.subscribed = subscribed
