# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApplicationSecurityWafExclusionFilterOnMatch(ModelSimple):
    """
    The action taken when the exclusion filter matches. When set to `monitor`, security traces are emitted but the requests are not blocked. By default, security traces are not emitted and the requests are not blocked.

    :param value: If omitted defaults to "monitor". Must be one of ["monitor"].
    :type value: str
    """

    allowed_values = {
        "monitor",
    }
    MONITOR: ClassVar["ApplicationSecurityWafExclusionFilterOnMatch"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApplicationSecurityWafExclusionFilterOnMatch.MONITOR = ApplicationSecurityWafExclusionFilterOnMatch("monitor")
