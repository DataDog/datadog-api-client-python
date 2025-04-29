# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSplunkHecDestinationType(ModelSimple):
    """
    The destination type. Always `splunk_hec`.

    :param value: If omitted defaults to "splunk_hec". Must be one of ["splunk_hec"].
    :type value: str
    """

    allowed_values = {
        "splunk_hec",
    }
    SPLUNK_HEC: ClassVar["ObservabilityPipelineSplunkHecDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSplunkHecDestinationType.SPLUNK_HEC = ObservabilityPipelineSplunkHecDestinationType("splunk_hec")
