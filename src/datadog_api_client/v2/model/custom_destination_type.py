# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomDestinationType(ModelSimple):
    """
    The type of the resource. The value should always be `custom_destination`.

    :param value: If omitted defaults to "custom_destination". Must be one of ["custom_destination"].
    :type value: str
    """

    allowed_values = {
        "custom_destination",
    }
    CUSTOM_DESTINATION: ClassVar["CustomDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomDestinationType.CUSTOM_DESTINATION = CustomDestinationType("custom_destination")
