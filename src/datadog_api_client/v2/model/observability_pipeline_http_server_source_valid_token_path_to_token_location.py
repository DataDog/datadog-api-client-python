# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineHttpServerSourceValidTokenPathToTokenLocation(ModelSimple):
    """
    Built-in token location on the incoming HTTP request.

    :param value: Must be one of ["path", "address"].
    :type value: str
    """

    allowed_values = {
        "path",
        "address",
    }
    PATH: ClassVar["ObservabilityPipelineHttpServerSourceValidTokenPathToTokenLocation"]
    ADDRESS: ClassVar["ObservabilityPipelineHttpServerSourceValidTokenPathToTokenLocation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineHttpServerSourceValidTokenPathToTokenLocation.PATH = (
    ObservabilityPipelineHttpServerSourceValidTokenPathToTokenLocation("path")
)
ObservabilityPipelineHttpServerSourceValidTokenPathToTokenLocation.ADDRESS = (
    ObservabilityPipelineHttpServerSourceValidTokenPathToTokenLocation("address")
)
