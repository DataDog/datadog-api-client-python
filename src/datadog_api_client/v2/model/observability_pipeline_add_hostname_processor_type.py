# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAddHostnameProcessorType(ModelSimple):
    """
    The processor type. The value should always be `add_hostname`.

    :param value: If omitted defaults to "add_hostname". Must be one of ["add_hostname"].
    :type value: str
    """

    allowed_values = {
        "add_hostname",
    }
    ADD_HOSTNAME: ClassVar["ObservabilityPipelineAddHostnameProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAddHostnameProcessorType.ADD_HOSTNAME = ObservabilityPipelineAddHostnameProcessorType(
    "add_hostname"
)
