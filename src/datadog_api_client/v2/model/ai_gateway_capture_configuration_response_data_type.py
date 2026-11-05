# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayCaptureConfigurationResponseDataType(ModelSimple):
    """
    Data capture configurations resource type.

    :param value: If omitted defaults to "data-capture-configurations". Must be one of ["data-capture-configurations"].
    :type value: str
    """

    allowed_values = {
        "data-capture-configurations",
    }
    DATA_CAPTURE_CONFIGURATIONS: ClassVar["AiGatewayCaptureConfigurationResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayCaptureConfigurationResponseDataType.DATA_CAPTURE_CONFIGURATIONS = (
    AiGatewayCaptureConfigurationResponseDataType("data-capture-configurations")
)
