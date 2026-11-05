# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayModelsByCanonicalType(ModelSimple):
    """
    Canonical model grouping resource type.

    :param value: If omitted defaults to "models-by-canonical". Must be one of ["models-by-canonical"].
    :type value: str
    """

    allowed_values = {
        "models-by-canonical",
    }
    MODELS_BY_CANONICAL: ClassVar["AiGatewayModelsByCanonicalType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayModelsByCanonicalType.MODELS_BY_CANONICAL = AiGatewayModelsByCanonicalType("models-by-canonical")
