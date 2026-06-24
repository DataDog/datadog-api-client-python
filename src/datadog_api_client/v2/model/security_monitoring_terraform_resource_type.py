# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringTerraformResourceType(ModelSimple):
    """
    The type of security monitoring resource to export to Terraform.

    :param value: Must be one of ["suppressions", "critical_assets", "security_filters", "rules"].
    :type value: str
    """

    allowed_values = {
        "suppressions",
        "critical_assets",
        "security_filters",
        "rules",
    }
    SUPPRESSIONS: ClassVar["SecurityMonitoringTerraformResourceType"]
    CRITICAL_ASSETS: ClassVar["SecurityMonitoringTerraformResourceType"]
    SECURITY_FILTERS: ClassVar["SecurityMonitoringTerraformResourceType"]
    RULES: ClassVar["SecurityMonitoringTerraformResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringTerraformResourceType.SUPPRESSIONS = SecurityMonitoringTerraformResourceType("suppressions")
SecurityMonitoringTerraformResourceType.CRITICAL_ASSETS = SecurityMonitoringTerraformResourceType("critical_assets")
SecurityMonitoringTerraformResourceType.SECURITY_FILTERS = SecurityMonitoringTerraformResourceType("security_filters")
SecurityMonitoringTerraformResourceType.RULES = SecurityMonitoringTerraformResourceType("rules")
