# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayCaptureCreateRequestDataAttributesMode(ModelSimple):
    """
    Capture mode for matching traffic.

    :param value: Must be one of ["metadata_only", "full_capture"].
    :type value: str
    """

    allowed_values = {
        "metadata_only",
        "full_capture",
    }
    METADATA_ONLY: ClassVar["AiGatewayCaptureCreateRequestDataAttributesMode"]
    FULL_CAPTURE: ClassVar["AiGatewayCaptureCreateRequestDataAttributesMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayCaptureCreateRequestDataAttributesMode.METADATA_ONLY = AiGatewayCaptureCreateRequestDataAttributesMode(
    "metadata_only"
)
AiGatewayCaptureCreateRequestDataAttributesMode.FULL_CAPTURE = AiGatewayCaptureCreateRequestDataAttributesMode(
    "full_capture"
)
