# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentAutomationDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    attribute_map = {
        "value": "value",
    }

    def __init__(self_, value: str, **kwargs):
        """
        Attributes for creating or updating automation data.

        :param value: The automation data value.
        :type value: str
        """
        super().__init__(kwargs)

        self_.value = value
