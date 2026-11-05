# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayModelMetadataStatus(ModelSimple):
    """
    Completeness of the matched source record. Partial also identifies metadata from a base model for a dated snapshot or from a shared canonical-model fallback.

    :param value: Must be one of ["available", "partial"].
    :type value: str
    """

    allowed_values = {
        "available",
        "partial",
    }
    AVAILABLE: ClassVar["AiGatewayModelMetadataStatus"]
    PARTIAL: ClassVar["AiGatewayModelMetadataStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayModelMetadataStatus.AVAILABLE = AiGatewayModelMetadataStatus("available")
AiGatewayModelMetadataStatus.PARTIAL = AiGatewayModelMetadataStatus("partial")
