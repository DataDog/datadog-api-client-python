# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MaxSessionDurationUpdateRequestDataType(ModelSimple):
    """
    Type of the resource.

    :param value: If omitted defaults to "max_session_duration". Must be one of ["max_session_duration"].
    :type value: str
    """

    allowed_values = {
        "max_session_duration",
    }
    MAX_SESSION_DURATION: ClassVar["MaxSessionDurationUpdateRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MaxSessionDurationUpdateRequestDataType.MAX_SESSION_DURATION = MaxSessionDurationUpdateRequestDataType(
    "max_session_duration"
)
