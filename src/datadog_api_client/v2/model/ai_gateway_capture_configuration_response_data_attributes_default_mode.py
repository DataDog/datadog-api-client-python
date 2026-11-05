# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode(ModelSimple):
    """
    Default capture mode for the organization. Change it in **Org defaults**.

    :param value: Must be one of ["metadata_only", "full_capture"].
    :type value: str
    """

    allowed_values = {
        "metadata_only",
        "full_capture",
    }
    METADATA_ONLY: ClassVar["AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode"]
    FULL_CAPTURE: ClassVar["AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode.METADATA_ONLY = (
    AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode("metadata_only")
)
AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode.FULL_CAPTURE = (
    AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode("full_capture")
)
