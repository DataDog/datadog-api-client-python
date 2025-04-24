# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineNewRelicDestinationType(ModelSimple):
    """
    The destination type. The value should always be `new_relic`.

    :param value: If omitted defaults to "new_relic". Must be one of ["new_relic"].
    :type value: str
    """

    allowed_values = {
        "new_relic",
    }
    NEW_RELIC: ClassVar["ObservabilityPipelineNewRelicDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineNewRelicDestinationType.NEW_RELIC = ObservabilityPipelineNewRelicDestinationType("new_relic")
