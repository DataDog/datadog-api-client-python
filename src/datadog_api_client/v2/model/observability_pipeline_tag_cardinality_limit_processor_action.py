# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineTagCardinalityLimitProcessorAction(ModelSimple):
    """
    The action to take when the cardinality limit is exceeded.

    :param value: Must be one of ["drop_tag", "drop_event"].
    :type value: str
    """

    allowed_values = {
        "drop_tag",
        "drop_event",
    }
    DROP_TAG: ClassVar["ObservabilityPipelineTagCardinalityLimitProcessorAction"]
    DROP_EVENT: ClassVar["ObservabilityPipelineTagCardinalityLimitProcessorAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineTagCardinalityLimitProcessorAction.DROP_TAG = (
    ObservabilityPipelineTagCardinalityLimitProcessorAction("drop_tag")
)
ObservabilityPipelineTagCardinalityLimitProcessorAction.DROP_EVENT = (
    ObservabilityPipelineTagCardinalityLimitProcessorAction("drop_event")
)
