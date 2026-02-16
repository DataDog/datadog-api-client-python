# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityFindingType(ModelSimple):
    """
    The type of security finding.

    :param value: Must be one of ["vulnerability", "configuration_finding"].
    :type value: str
    """

    allowed_values = {
        "vulnerability",
        "configuration_finding",
    }
    VULNERABILITY: ClassVar["SecurityFindingType"]
    CONFIGURATION_FINDING: ClassVar["SecurityFindingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityFindingType.VULNERABILITY = SecurityFindingType("vulnerability")
SecurityFindingType.CONFIGURATION_FINDING = SecurityFindingType("configuration_finding")
