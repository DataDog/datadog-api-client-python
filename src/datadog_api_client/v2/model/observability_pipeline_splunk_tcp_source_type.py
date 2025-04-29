# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSplunkTcpSourceType(ModelSimple):
    """
    The source type. Always `splunk_tcp`.

    :param value: If omitted defaults to "splunk_tcp". Must be one of ["splunk_tcp"].
    :type value: str
    """

    allowed_values = {
        "splunk_tcp",
    }
    SPLUNK_TCP: ClassVar["ObservabilityPipelineSplunkTcpSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSplunkTcpSourceType.SPLUNK_TCP = ObservabilityPipelineSplunkTcpSourceType("splunk_tcp")
