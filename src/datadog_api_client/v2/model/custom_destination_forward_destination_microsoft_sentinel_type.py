# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomDestinationForwardDestinationMicrosoftSentinelType(ModelSimple):
    """
    Type of the Microsoft Sentinel destination.

    :param value: If omitted defaults to "microsoft_sentinel". Must be one of ["microsoft_sentinel"].
    :type value: str
    """

    allowed_values = {
        "microsoft_sentinel",
    }
    MICROSOFT_SENTINEL: ClassVar["CustomDestinationForwardDestinationMicrosoftSentinelType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomDestinationForwardDestinationMicrosoftSentinelType.MICROSOFT_SENTINEL = (
    CustomDestinationForwardDestinationMicrosoftSentinelType("microsoft_sentinel")
)
