# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineGoogleChronicleDestinationType(ModelSimple):
    """
    The destination type. The value should always be `google_chronicle`.

    :param value: If omitted defaults to "google_chronicle". Must be one of ["google_chronicle"].
    :type value: str
    """

    allowed_values = {
        "google_chronicle",
    }
    GOOGLE_CHRONICLE: ClassVar["ObservabilityPipelineGoogleChronicleDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineGoogleChronicleDestinationType.GOOGLE_CHRONICLE = (
    ObservabilityPipelineGoogleChronicleDestinationType("google_chronicle")
)
