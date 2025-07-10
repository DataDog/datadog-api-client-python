# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSocketSourceFramingOctetCountingMethod(ModelSimple):
    """
    Byte frames according to the octet counting format as per RFC6587.

    :param value: If omitted defaults to "octet_counting". Must be one of ["octet_counting"].
    :type value: str
    """

    allowed_values = {
        "octet_counting",
    }
    OCTET_COUNTING: ClassVar["ObservabilityPipelineSocketSourceFramingOctetCountingMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSocketSourceFramingOctetCountingMethod.OCTET_COUNTING = (
    ObservabilityPipelineSocketSourceFramingOctetCountingMethod("octet_counting")
)
