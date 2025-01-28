# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityRuleTypesItems(ModelSimple):
    """
    Security rule type

    :param value: Must be one of ["application_code_vulnerability", "application_library_vulnerability", "attack_path", "container_image_vulnerability", "host_vulnerability", "identity_risk", "misconfiguration", "api_security"].
    :type value: str
    """

    allowed_values = {
        "application_code_vulnerability",
        "application_library_vulnerability",
        "attack_path",
        "container_image_vulnerability",
        "host_vulnerability",
        "identity_risk",
        "misconfiguration",
        "api_security",
    }
    APPLICATION_CODE_VULNERABILITY: ClassVar["SecurityRuleTypesItems"]
    APPLICATION_LIBRARY_VULNERABILITY: ClassVar["SecurityRuleTypesItems"]
    ATTACK_PATH: ClassVar["SecurityRuleTypesItems"]
    CONTAINER_IMAGE_VULNERABILITY: ClassVar["SecurityRuleTypesItems"]
    HOST_VULNERABILITY: ClassVar["SecurityRuleTypesItems"]
    IDENTITY_RISK: ClassVar["SecurityRuleTypesItems"]
    MISCONFIGURATION: ClassVar["SecurityRuleTypesItems"]
    API_SECURITY: ClassVar["SecurityRuleTypesItems"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityRuleTypesItems.APPLICATION_CODE_VULNERABILITY = SecurityRuleTypesItems("application_code_vulnerability")
SecurityRuleTypesItems.APPLICATION_LIBRARY_VULNERABILITY = SecurityRuleTypesItems("application_library_vulnerability")
SecurityRuleTypesItems.ATTACK_PATH = SecurityRuleTypesItems("attack_path")
SecurityRuleTypesItems.CONTAINER_IMAGE_VULNERABILITY = SecurityRuleTypesItems("container_image_vulnerability")
SecurityRuleTypesItems.HOST_VULNERABILITY = SecurityRuleTypesItems("host_vulnerability")
SecurityRuleTypesItems.IDENTITY_RISK = SecurityRuleTypesItems("identity_risk")
SecurityRuleTypesItems.MISCONFIGURATION = SecurityRuleTypesItems("misconfiguration")
SecurityRuleTypesItems.API_SECURITY = SecurityRuleTypesItems("api_security")
