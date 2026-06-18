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
    The type of security finding that the automation rule applies to.

    :param value: Must be one of ["api_security", "attack_path", "host_and_container_vulnerability", "iac_misconfiguration", "identity_risk", "library_vulnerability", "misconfiguration", "runtime_code_vulnerability", "secret", "static_code_vulnerability", "workload_activity"].
    :type value: str
    """

    allowed_values = {
        "api_security",
        "attack_path",
        "host_and_container_vulnerability",
        "iac_misconfiguration",
        "identity_risk",
        "library_vulnerability",
        "misconfiguration",
        "runtime_code_vulnerability",
        "secret",
        "static_code_vulnerability",
        "workload_activity",
    }
    API_SECURITY: ClassVar["SecurityFindingType"]
    ATTACK_PATH: ClassVar["SecurityFindingType"]
    HOST_AND_CONTAINER_VULNERABILITY: ClassVar["SecurityFindingType"]
    IAC_MISCONFIGURATION: ClassVar["SecurityFindingType"]
    IDENTITY_RISK: ClassVar["SecurityFindingType"]
    LIBRARY_VULNERABILITY: ClassVar["SecurityFindingType"]
    MISCONFIGURATION: ClassVar["SecurityFindingType"]
    RUNTIME_CODE_VULNERABILITY: ClassVar["SecurityFindingType"]
    SECRET: ClassVar["SecurityFindingType"]
    STATIC_CODE_VULNERABILITY: ClassVar["SecurityFindingType"]
    WORKLOAD_ACTIVITY: ClassVar["SecurityFindingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityFindingType.API_SECURITY = SecurityFindingType("api_security")
SecurityFindingType.ATTACK_PATH = SecurityFindingType("attack_path")
SecurityFindingType.HOST_AND_CONTAINER_VULNERABILITY = SecurityFindingType("host_and_container_vulnerability")
SecurityFindingType.IAC_MISCONFIGURATION = SecurityFindingType("iac_misconfiguration")
SecurityFindingType.IDENTITY_RISK = SecurityFindingType("identity_risk")
SecurityFindingType.LIBRARY_VULNERABILITY = SecurityFindingType("library_vulnerability")
SecurityFindingType.MISCONFIGURATION = SecurityFindingType("misconfiguration")
SecurityFindingType.RUNTIME_CODE_VULNERABILITY = SecurityFindingType("runtime_code_vulnerability")
SecurityFindingType.SECRET = SecurityFindingType("secret")
SecurityFindingType.STATIC_CODE_VULNERABILITY = SecurityFindingType("static_code_vulnerability")
SecurityFindingType.WORKLOAD_ACTIVITY = SecurityFindingType("workload_activity")
