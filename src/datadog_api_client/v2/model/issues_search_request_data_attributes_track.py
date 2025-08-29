# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssuesSearchRequestDataAttributesTrack(ModelSimple):
    """
    Track of the events to query. Either track(s) or persona(s) must be specified.

    :param value: Must be one of ["trace", "logs", "rum"].
    :type value: str
    """

    allowed_values = {
        "trace",
        "logs",
        "rum",
    }
    TRACE: ClassVar["IssuesSearchRequestDataAttributesTrack"]
    LOGS: ClassVar["IssuesSearchRequestDataAttributesTrack"]
    RUM: ClassVar["IssuesSearchRequestDataAttributesTrack"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssuesSearchRequestDataAttributesTrack.TRACE = IssuesSearchRequestDataAttributesTrack("trace")
IssuesSearchRequestDataAttributesTrack.LOGS = IssuesSearchRequestDataAttributesTrack("logs")
IssuesSearchRequestDataAttributesTrack.RUM = IssuesSearchRequestDataAttributesTrack("rum")
