# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayCaptureOverrideResponseDataAttributesMode(ModelSimple):
    """
    Capture mode for matching traffic.

    :param value: Must be one of ["metadata_only", "full_capture"].
    :type value: str
    """

    allowed_values = {
        "metadata_only",
        "full_capture",
    }
    METADATA_ONLY: ClassVar["AiGatewayCaptureOverrideResponseDataAttributesMode"]
    FULL_CAPTURE: ClassVar["AiGatewayCaptureOverrideResponseDataAttributesMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayCaptureOverrideResponseDataAttributesMode.METADATA_ONLY = AiGatewayCaptureOverrideResponseDataAttributesMode(
    "metadata_only"
)
AiGatewayCaptureOverrideResponseDataAttributesMode.FULL_CAPTURE = AiGatewayCaptureOverrideResponseDataAttributesMode(
    "full_capture"
)
