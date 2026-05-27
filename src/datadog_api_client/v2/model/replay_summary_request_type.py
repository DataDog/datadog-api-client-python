# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ReplaySummaryRequestType(ModelSimple):
    """
    RUM replay summary request resource type.

    :param value: If omitted defaults to "replay_summary_request". Must be one of ["replay_summary_request"].
    :type value: str
    """

    allowed_values = {
        "replay_summary_request",
    }
    REPLAY_SUMMARY_REQUEST: ClassVar["ReplaySummaryRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ReplaySummaryRequestType.REPLAY_SUMMARY_REQUEST = ReplaySummaryRequestType("replay_summary_request")
