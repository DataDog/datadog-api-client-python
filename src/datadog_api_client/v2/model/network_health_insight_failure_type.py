# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NetworkHealthInsightFailureType(ModelSimple):
    """
    Specific failure type within the insight category. For DNS insights: `timeout`, `nxdomain`,
        `servfail`, or `general_failure`. For TLS certificate insights: `expired` or `expiring_soon`.
        For security group insights: `denied`.

    :param value: Must be one of ["timeout", "nxdomain", "servfail", "general_failure", "expired", "expiring_soon", "denied"].
    :type value: str
    """

    allowed_values = {
        "timeout",
        "nxdomain",
        "servfail",
        "general_failure",
        "expired",
        "expiring_soon",
        "denied",
    }
    TIMEOUT: ClassVar["NetworkHealthInsightFailureType"]
    NXDOMAIN: ClassVar["NetworkHealthInsightFailureType"]
    SERVFAIL: ClassVar["NetworkHealthInsightFailureType"]
    GENERAL_FAILURE: ClassVar["NetworkHealthInsightFailureType"]
    EXPIRED: ClassVar["NetworkHealthInsightFailureType"]
    EXPIRING_SOON: ClassVar["NetworkHealthInsightFailureType"]
    DENIED: ClassVar["NetworkHealthInsightFailureType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NetworkHealthInsightFailureType.TIMEOUT = NetworkHealthInsightFailureType("timeout")
NetworkHealthInsightFailureType.NXDOMAIN = NetworkHealthInsightFailureType("nxdomain")
NetworkHealthInsightFailureType.SERVFAIL = NetworkHealthInsightFailureType("servfail")
NetworkHealthInsightFailureType.GENERAL_FAILURE = NetworkHealthInsightFailureType("general_failure")
NetworkHealthInsightFailureType.EXPIRED = NetworkHealthInsightFailureType("expired")
NetworkHealthInsightFailureType.EXPIRING_SOON = NetworkHealthInsightFailureType("expiring_soon")
NetworkHealthInsightFailureType.DENIED = NetworkHealthInsightFailureType("denied")
