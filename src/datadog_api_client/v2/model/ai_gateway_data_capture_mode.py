# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayDataCaptureMode(ModelSimple):
    """
    Controls whether AI Gateway captures request and response content in addition to metadata.

    :param value: Must be one of ["metadata_only", "full_capture"].
    :type value: str
    """

    allowed_values = {
        "metadata_only",
        "full_capture",
    }
    METADATA_ONLY: ClassVar["AiGatewayDataCaptureMode"]
    FULL_CAPTURE: ClassVar["AiGatewayDataCaptureMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayDataCaptureMode.METADATA_ONLY = AiGatewayDataCaptureMode("metadata_only")
AiGatewayDataCaptureMode.FULL_CAPTURE = AiGatewayDataCaptureMode("full_capture")
