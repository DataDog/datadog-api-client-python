# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleConvertBulkDataType(ModelSimple):
    """
    The type of the resource.

    :param value: If omitted defaults to "security_monitoring_rules_convert_bulk". Must be one of ["security_monitoring_rules_convert_bulk"].
    :type value: str
    """

    allowed_values = {
        "security_monitoring_rules_convert_bulk",
    }
    SECURITY_MONITORING_RULES_CONVERT_BULK: ClassVar["SecurityMonitoringRuleConvertBulkDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringRuleConvertBulkDataType.SECURITY_MONITORING_RULES_CONVERT_BULK = (
    SecurityMonitoringRuleConvertBulkDataType("security_monitoring_rules_convert_bulk")
)
