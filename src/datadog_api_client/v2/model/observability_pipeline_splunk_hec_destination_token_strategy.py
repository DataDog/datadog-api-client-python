# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSplunkHecDestinationTokenStrategy(ModelSimple):
    """
    Controls how the Splunk HEC token is supplied. Use `custom` to provide a token with `token_key`, or `from_source` to forward the token received from an upstream Splunk HEC source.

    :param value: Must be one of ["custom", "from_source"].
    :type value: str
    """

    allowed_values = {
        "custom",
        "from_source",
    }
    CUSTOM: ClassVar["ObservabilityPipelineSplunkHecDestinationTokenStrategy"]
    FROM_SOURCE: ClassVar["ObservabilityPipelineSplunkHecDestinationTokenStrategy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSplunkHecDestinationTokenStrategy.CUSTOM = ObservabilityPipelineSplunkHecDestinationTokenStrategy(
    "custom"
)
ObservabilityPipelineSplunkHecDestinationTokenStrategy.FROM_SOURCE = (
    ObservabilityPipelineSplunkHecDestinationTokenStrategy("from_source")
)
