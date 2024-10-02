# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FindingDetectionType(ModelSimple):
    """
    The detection type of the finding.

    :param value: Must be one of ["misconfiguration", "attack_path", "identity_risk", "api_security"].
    :type value: str
    """

    allowed_values = {
        "misconfiguration",
        "attack_path",
        "identity_risk",
        "api_security",
    }
    MISCONFIGURATION: ClassVar["FindingDetectionType"]
    ATTACK_PATH: ClassVar["FindingDetectionType"]
    IDENTITY_RISK: ClassVar["FindingDetectionType"]
    API_SECURITY: ClassVar["FindingDetectionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FindingDetectionType.MISCONFIGURATION = FindingDetectionType("misconfiguration")
FindingDetectionType.ATTACK_PATH = FindingDetectionType("attack_path")
FindingDetectionType.IDENTITY_RISK = FindingDetectionType("identity_risk")
FindingDetectionType.API_SECURITY = FindingDetectionType("api_security")
