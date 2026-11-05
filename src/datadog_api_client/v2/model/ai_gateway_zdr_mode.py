# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayZDRMode(ModelSimple):
    """
    Zero data retention requirement for the organization's requests.

    :param value: Must be one of ["off", "required"].
    :type value: str
    """

    allowed_values = {
        "off",
        "required",
    }
    OFF: ClassVar["AiGatewayZDRMode"]
    REQUIRED: ClassVar["AiGatewayZDRMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayZDRMode.OFF = AiGatewayZDRMode("off")
AiGatewayZDRMode.REQUIRED = AiGatewayZDRMode("required")
