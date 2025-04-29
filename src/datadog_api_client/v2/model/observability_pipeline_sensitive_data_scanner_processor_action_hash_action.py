# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSensitiveDataScannerProcessorActionHashAction(ModelSimple):
    """
    Action type that replaces the matched sensitive data with a hashed representation, preserving structure while securing content.

    :param value: If omitted defaults to "hash". Must be one of ["hash"].
    :type value: str
    """

    allowed_values = {
        "hash",
    }
    HASH: ClassVar["ObservabilityPipelineSensitiveDataScannerProcessorActionHashAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSensitiveDataScannerProcessorActionHashAction.HASH = (
    ObservabilityPipelineSensitiveDataScannerProcessorActionHashAction("hash")
)
