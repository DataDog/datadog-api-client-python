# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MicrosoftSentinelDestinationType(ModelSimple):
    """
    The destination type. The value should always be `microsoft_sentinel`.

    :param value: If omitted defaults to "microsoft_sentinel". Must be one of ["microsoft_sentinel"].
    :type value: str
    """

    allowed_values = {
        "microsoft_sentinel",
    }
    MICROSOFT_SENTINEL: ClassVar["MicrosoftSentinelDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MicrosoftSentinelDestinationType.MICROSOFT_SENTINEL = MicrosoftSentinelDestinationType("microsoft_sentinel")
