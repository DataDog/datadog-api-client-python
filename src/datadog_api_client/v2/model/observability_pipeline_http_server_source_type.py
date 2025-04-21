# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineHttpServerSourceType(ModelSimple):
    """
    The source type. The value should always be `http_server`.

    :param value: If omitted defaults to "http_server". Must be one of ["http_server"].
    :type value: str
    """

    allowed_values = {
        "http_server",
    }
    HTTP_SERVER: ClassVar["ObservabilityPipelineHttpServerSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineHttpServerSourceType.HTTP_SERVER = ObservabilityPipelineHttpServerSourceType("http_server")
