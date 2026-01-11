# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineHttpClientSourceAuthStrategy(ModelSimple):
    """
    Optional authentication strategy for HTTP requests.

    :param value: Must be one of ["none", "basic", "bearer"].
    :type value: str
    """

    allowed_values = {
        "none",
        "basic",
        "bearer",
    }
    NONE: ClassVar["ObservabilityPipelineHttpClientSourceAuthStrategy"]
    BASIC: ClassVar["ObservabilityPipelineHttpClientSourceAuthStrategy"]
    BEARER: ClassVar["ObservabilityPipelineHttpClientSourceAuthStrategy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineHttpClientSourceAuthStrategy.NONE = ObservabilityPipelineHttpClientSourceAuthStrategy("none")
ObservabilityPipelineHttpClientSourceAuthStrategy.BASIC = ObservabilityPipelineHttpClientSourceAuthStrategy("basic")
ObservabilityPipelineHttpClientSourceAuthStrategy.BEARER = ObservabilityPipelineHttpClientSourceAuthStrategy("bearer")
