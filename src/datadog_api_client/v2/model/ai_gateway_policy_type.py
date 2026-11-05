# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayPolicyType(ModelSimple):
    """
    AI Gateway routing policy resource type.

    :param value: If omitted defaults to "routing-documents". Must be one of ["routing-documents"].
    :type value: str
    """

    allowed_values = {
        "routing-documents",
    }
    ROUTING_DOCUMENTS: ClassVar["AiGatewayPolicyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayPolicyType.ROUTING_DOCUMENTS = AiGatewayPolicyType("routing-documents")
