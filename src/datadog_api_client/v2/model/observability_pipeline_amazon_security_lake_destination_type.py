# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAmazonSecurityLakeDestinationType(ModelSimple):
    """
    The destination type. Always `amazon_security_lake`.

    :param value: If omitted defaults to "amazon_security_lake". Must be one of ["amazon_security_lake"].
    :type value: str
    """

    allowed_values = {
        "amazon_security_lake",
    }
    AMAZON_SECURITY_LAKE: ClassVar["ObservabilityPipelineAmazonSecurityLakeDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAmazonSecurityLakeDestinationType.AMAZON_SECURITY_LAKE = (
    ObservabilityPipelineAmazonSecurityLakeDestinationType("amazon_security_lake")
)
