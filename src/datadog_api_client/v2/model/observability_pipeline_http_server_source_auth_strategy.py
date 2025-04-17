# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineHttpServerSourceAuthStrategy(ModelSimple):
    """
    HTTP authentication method.

    :param value: Must be one of ["none", "plain"].
    :type value: str
    """

    allowed_values = {
        "none",
        "plain",
    }
    NONE: ClassVar["ObservabilityPipelineHttpServerSourceAuthStrategy"]
    PLAIN: ClassVar["ObservabilityPipelineHttpServerSourceAuthStrategy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineHttpServerSourceAuthStrategy.NONE = ObservabilityPipelineHttpServerSourceAuthStrategy("none")
ObservabilityPipelineHttpServerSourceAuthStrategy.PLAIN = ObservabilityPipelineHttpServerSourceAuthStrategy("plain")
