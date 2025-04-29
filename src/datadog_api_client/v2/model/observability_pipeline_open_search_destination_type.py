# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineOpenSearchDestinationType(ModelSimple):
    """
    The destination type. The value should always be `opensearch`.

    :param value: If omitted defaults to "opensearch". Must be one of ["opensearch"].
    :type value: str
    """

    allowed_values = {
        "opensearch",
    }
    OPENSEARCH: ClassVar["ObservabilityPipelineOpenSearchDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineOpenSearchDestinationType.OPENSEARCH = ObservabilityPipelineOpenSearchDestinationType("opensearch")
