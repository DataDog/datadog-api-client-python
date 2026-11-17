# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayModelZdrCoverage(ModelSimple):
    """
    Datadog's coverage of the model's operations under zero data retention. A model is eligible when
        coverage is `full` and its provider's `zdr_eligible` is `true`. `partial` means only the
        `covered_operations` can be served: requests on other operations are not dispatched to it.

    :param value: Must be one of ["full", "partial", "none"].
    :type value: str
    """

    allowed_values = {
        "full",
        "partial",
        "none",
    }
    FULL: ClassVar["AiGatewayModelZdrCoverage"]
    PARTIAL: ClassVar["AiGatewayModelZdrCoverage"]
    NONE: ClassVar["AiGatewayModelZdrCoverage"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayModelZdrCoverage.FULL = AiGatewayModelZdrCoverage("full")
AiGatewayModelZdrCoverage.PARTIAL = AiGatewayModelZdrCoverage("partial")
AiGatewayModelZdrCoverage.NONE = AiGatewayModelZdrCoverage("none")
