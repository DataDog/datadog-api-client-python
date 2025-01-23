# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RuleTypesItems(ModelSimple):
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
    APPLICATION_CODE_VULNERABILITY: ClassVar["RuleTypesItems"]
    APPLICATION_LIBRARY_VULNERABILITY: ClassVar["RuleTypesItems"]
    ATTACK_PATH: ClassVar["RuleTypesItems"]
    CONTAINER_IMAGE_VULNERABILITY: ClassVar["RuleTypesItems"]
    HOST_VULNERABILITY: ClassVar["RuleTypesItems"]
    IDENTITY_RISK: ClassVar["RuleTypesItems"]
    MISCONFIGURATION: ClassVar["RuleTypesItems"]
    API_SECURITY: ClassVar["RuleTypesItems"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RuleTypesItems.APPLICATION_CODE_VULNERABILITY = RuleTypesItems("application_code_vulnerability")
RuleTypesItems.APPLICATION_LIBRARY_VULNERABILITY = RuleTypesItems("application_library_vulnerability")
RuleTypesItems.ATTACK_PATH = RuleTypesItems("attack_path")
RuleTypesItems.CONTAINER_IMAGE_VULNERABILITY = RuleTypesItems("container_image_vulnerability")
RuleTypesItems.HOST_VULNERABILITY = RuleTypesItems("host_vulnerability")
RuleTypesItems.IDENTITY_RISK = RuleTypesItems("identity_risk")
RuleTypesItems.MISCONFIGURATION = RuleTypesItems("misconfiguration")
RuleTypesItems.API_SECURITY = RuleTypesItems("api_security")
