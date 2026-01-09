# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineHttpClientDestinationAuthStrategy(ModelSimple):
    """
    HTTP authentication strategy.

    :param value: Must be one of ["none", "basic", "bearer"].
    :type value: str
    """

    allowed_values = {
        "none",
        "basic",
        "bearer",
    }
    NONE: ClassVar["ObservabilityPipelineHttpClientDestinationAuthStrategy"]
    BASIC: ClassVar["ObservabilityPipelineHttpClientDestinationAuthStrategy"]
    BEARER: ClassVar["ObservabilityPipelineHttpClientDestinationAuthStrategy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineHttpClientDestinationAuthStrategy.NONE = ObservabilityPipelineHttpClientDestinationAuthStrategy(
    "none"
)
ObservabilityPipelineHttpClientDestinationAuthStrategy.BASIC = ObservabilityPipelineHttpClientDestinationAuthStrategy(
    "basic"
)
ObservabilityPipelineHttpClientDestinationAuthStrategy.BEARER = ObservabilityPipelineHttpClientDestinationAuthStrategy(
    "bearer"
)
