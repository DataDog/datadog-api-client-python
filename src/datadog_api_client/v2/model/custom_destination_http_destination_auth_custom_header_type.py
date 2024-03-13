# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomDestinationHttpDestinationAuthCustomHeaderType(ModelSimple):
    """
    Type of the custom header access authentication.

    :param value: If omitted defaults to "custom_header". Must be one of ["custom_header"].
    :type value: str
    """

    allowed_values = {
        "custom_header",
    }
    CUSTOM_HEADER: ClassVar["CustomDestinationHttpDestinationAuthCustomHeaderType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomDestinationHttpDestinationAuthCustomHeaderType.CUSTOM_HEADER = (
    CustomDestinationHttpDestinationAuthCustomHeaderType("custom_header")
)
