# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineHttpClientSourceType(ModelSimple):
    """
    The source type. The value should always be `http_client`.

    :param value: If omitted defaults to "http_client". Must be one of ["http_client"].
    :type value: str
    """

    allowed_values = {
        "http_client",
    }
    HTTP_CLIENT: ClassVar["ObservabilityPipelineHttpClientSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineHttpClientSourceType.HTTP_CLIENT = ObservabilityPipelineHttpClientSourceType("http_client")
