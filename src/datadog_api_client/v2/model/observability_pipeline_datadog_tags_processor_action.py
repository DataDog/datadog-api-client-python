# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineDatadogTagsProcessorAction(ModelSimple):
    """
    The action to take on tags with matching keys.

    :param value: Must be one of ["include", "exclude"].
    :type value: str
    """

    allowed_values = {
        "include",
        "exclude",
    }
    INCLUDE: ClassVar["ObservabilityPipelineDatadogTagsProcessorAction"]
    EXCLUDE: ClassVar["ObservabilityPipelineDatadogTagsProcessorAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineDatadogTagsProcessorAction.INCLUDE = ObservabilityPipelineDatadogTagsProcessorAction("include")
ObservabilityPipelineDatadogTagsProcessorAction.EXCLUDE = ObservabilityPipelineDatadogTagsProcessorAction("exclude")
