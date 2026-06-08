# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRateLimitQuotaReachedAction(ModelSimple):
    """
    The action to take when the session quota is reached.

    :param value: Must be one of ["stop", "slowdown"].
    :type value: str
    """

    allowed_values = {
        "stop",
        "slowdown",
    }
    STOP: ClassVar["RumRateLimitQuotaReachedAction"]
    SLOWDOWN: ClassVar["RumRateLimitQuotaReachedAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRateLimitQuotaReachedAction.STOP = RumRateLimitQuotaReachedAction("stop")
RumRateLimitQuotaReachedAction.SLOWDOWN = RumRateLimitQuotaReachedAction("slowdown")
