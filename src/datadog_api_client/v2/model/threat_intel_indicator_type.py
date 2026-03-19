# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ThreatIntelIndicatorType(ModelSimple):
    """
    The type of threat indicator.

    :param value: Must be one of ["ip_address", "domain", "sha256"].
    :type value: str
    """

    allowed_values = {
        "ip_address",
        "domain",
        "sha256",
    }
    IP_ADDRESS: ClassVar["ThreatIntelIndicatorType"]
    DOMAIN: ClassVar["ThreatIntelIndicatorType"]
    SHA256: ClassVar["ThreatIntelIndicatorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ThreatIntelIndicatorType.IP_ADDRESS = ThreatIntelIndicatorType("ip_address")
ThreatIntelIndicatorType.DOMAIN = ThreatIntelIndicatorType("domain")
ThreatIntelIndicatorType.SHA256 = ThreatIntelIndicatorType("sha256")
