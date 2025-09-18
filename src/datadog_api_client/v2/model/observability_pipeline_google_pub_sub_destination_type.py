# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineGooglePubSubDestinationType(ModelSimple):
    """
    The destination type. The value should always be `google_pubsub`.

    :param value: If omitted defaults to "google_pubsub". Must be one of ["google_pubsub"].
    :type value: str
    """

    allowed_values = {
        "google_pubsub",
    }
    GOOGLE_PUBSUB: ClassVar["ObservabilityPipelineGooglePubSubDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineGooglePubSubDestinationType.GOOGLE_PUBSUB = ObservabilityPipelineGooglePubSubDestinationType(
    "google_pubsub"
)
