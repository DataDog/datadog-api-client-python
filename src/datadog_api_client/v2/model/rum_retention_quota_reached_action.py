# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRetentionQuotaReachedAction(ModelSimple):
    """
    The action to take when the session quota is reached.

    :param value: Must be one of ["stop", "slowdown"].
    :type value: str
    """

    allowed_values = {
        "stop",
        "slowdown",
    }
    STOP: ClassVar["RumRetentionQuotaReachedAction"]
    SLOWDOWN: ClassVar["RumRetentionQuotaReachedAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRetentionQuotaReachedAction.STOP = RumRetentionQuotaReachedAction("stop")
RumRetentionQuotaReachedAction.SLOWDOWN = RumRetentionQuotaReachedAction("slowdown")
