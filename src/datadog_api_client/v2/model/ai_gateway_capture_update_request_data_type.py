# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayCaptureUpdateRequestDataType(ModelSimple):
    """
    Data capture overrides resource type.

    :param value: If omitted defaults to "data-capture-overrides". Must be one of ["data-capture-overrides"].
    :type value: str
    """

    allowed_values = {
        "data-capture-overrides",
    }
    DATA_CAPTURE_OVERRIDES: ClassVar["AiGatewayCaptureUpdateRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayCaptureUpdateRequestDataType.DATA_CAPTURE_OVERRIDES = AiGatewayCaptureUpdateRequestDataType(
    "data-capture-overrides"
)
