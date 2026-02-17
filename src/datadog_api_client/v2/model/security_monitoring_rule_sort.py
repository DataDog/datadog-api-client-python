# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleSort(ModelSimple):
    """
    The sort parameters used for querying security monitoring rules.

    :param value: Must be one of ["name", "creation_date", "update_date", "enabled", "type", "highest_severity", "source", "-name", "-creation_date", "-update_date", "-enabled", "-type", "-highest_severity", "-source"].
    :type value: str
    """

    allowed_values = {
        "name",
        "creation_date",
        "update_date",
        "enabled",
        "type",
        "highest_severity",
        "source",
        "-name",
        "-creation_date",
        "-update_date",
        "-enabled",
        "-type",
        "-highest_severity",
        "-source",
    }
    NAME: ClassVar["SecurityMonitoringRuleSort"]
    CREATION_DATE: ClassVar["SecurityMonitoringRuleSort"]
    UPDATE_DATE: ClassVar["SecurityMonitoringRuleSort"]
    ENABLED: ClassVar["SecurityMonitoringRuleSort"]
    TYPE: ClassVar["SecurityMonitoringRuleSort"]
    HIGHEST_SEVERITY: ClassVar["SecurityMonitoringRuleSort"]
    SOURCE: ClassVar["SecurityMonitoringRuleSort"]
    NAME_DESCENDING: ClassVar["SecurityMonitoringRuleSort"]
    CREATION_DATE_DESCENDING: ClassVar["SecurityMonitoringRuleSort"]
    UPDATE_DATE_DESCENDING: ClassVar["SecurityMonitoringRuleSort"]
    ENABLED_DESCENDING: ClassVar["SecurityMonitoringRuleSort"]
    TYPE_DESCENDING: ClassVar["SecurityMonitoringRuleSort"]
    HIGHEST_SEVERITY_DESCENDING: ClassVar["SecurityMonitoringRuleSort"]
    SOURCE_DESCENDING: ClassVar["SecurityMonitoringRuleSort"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringRuleSort.NAME = SecurityMonitoringRuleSort("name")
SecurityMonitoringRuleSort.CREATION_DATE = SecurityMonitoringRuleSort("creation_date")
SecurityMonitoringRuleSort.UPDATE_DATE = SecurityMonitoringRuleSort("update_date")
SecurityMonitoringRuleSort.ENABLED = SecurityMonitoringRuleSort("enabled")
SecurityMonitoringRuleSort.TYPE = SecurityMonitoringRuleSort("type")
SecurityMonitoringRuleSort.HIGHEST_SEVERITY = SecurityMonitoringRuleSort("highest_severity")
SecurityMonitoringRuleSort.SOURCE = SecurityMonitoringRuleSort("source")
SecurityMonitoringRuleSort.NAME_DESCENDING = SecurityMonitoringRuleSort("-name")
SecurityMonitoringRuleSort.CREATION_DATE_DESCENDING = SecurityMonitoringRuleSort("-creation_date")
SecurityMonitoringRuleSort.UPDATE_DATE_DESCENDING = SecurityMonitoringRuleSort("-update_date")
SecurityMonitoringRuleSort.ENABLED_DESCENDING = SecurityMonitoringRuleSort("-enabled")
SecurityMonitoringRuleSort.TYPE_DESCENDING = SecurityMonitoringRuleSort("-type")
SecurityMonitoringRuleSort.HIGHEST_SEVERITY_DESCENDING = SecurityMonitoringRuleSort("-highest_severity")
SecurityMonitoringRuleSort.SOURCE_DESCENDING = SecurityMonitoringRuleSort("-source")
