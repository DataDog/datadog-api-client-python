# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NetworkHealthInsightCategory(ModelSimple):
    """
    Category of network health insight. Indicates whether the insight relates to a DNS issue (`dns`),
        a TCP issue (`tcp`), a TLS certificate issue (`tls-cert`), or a security group denial (`security-group`).

    :param value: Must be one of ["dns", "tcp", "tls-cert", "security-group"].
    :type value: str
    """

    allowed_values = {
        "dns",
        "tcp",
        "tls-cert",
        "security-group",
    }
    DNS: ClassVar["NetworkHealthInsightCategory"]
    TCP: ClassVar["NetworkHealthInsightCategory"]
    TLS_CERT: ClassVar["NetworkHealthInsightCategory"]
    SECURITY_GROUP: ClassVar["NetworkHealthInsightCategory"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NetworkHealthInsightCategory.DNS = NetworkHealthInsightCategory("dns")
NetworkHealthInsightCategory.TCP = NetworkHealthInsightCategory("tcp")
NetworkHealthInsightCategory.TLS_CERT = NetworkHealthInsightCategory("tls-cert")
NetworkHealthInsightCategory.SECURITY_GROUP = NetworkHealthInsightCategory("security-group")
