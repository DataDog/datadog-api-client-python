# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringSuppressionSort(ModelSimple):
    """
    The sort parameters used for querying suppression rules.

    :param value: Must be one of ["name", "start_date", "expiration_date", "update_date", "enabled", "-name", "-start_date", "-expiration_date", "-update_date", "-creation_date", "-enabled"].
    :type value: str
    """

    allowed_values = {
        "name",
        "start_date",
        "expiration_date",
        "update_date",
        "enabled",
        "-name",
        "-start_date",
        "-expiration_date",
        "-update_date",
        "-creation_date",
        "-enabled",
    }
    NAME: ClassVar["SecurityMonitoringSuppressionSort"]
    START_DATE: ClassVar["SecurityMonitoringSuppressionSort"]
    EXPIRATION_DATE: ClassVar["SecurityMonitoringSuppressionSort"]
    UPDATE_DATE: ClassVar["SecurityMonitoringSuppressionSort"]
    ENABLED: ClassVar["SecurityMonitoringSuppressionSort"]
    NAME_DESCENDING: ClassVar["SecurityMonitoringSuppressionSort"]
    START_DATE_DESCENDING: ClassVar["SecurityMonitoringSuppressionSort"]
    EXPIRATION_DATE_DESCENDING: ClassVar["SecurityMonitoringSuppressionSort"]
    UPDATE_DATE_DESCENDING: ClassVar["SecurityMonitoringSuppressionSort"]
    CREATION_DATE_DESCENDING: ClassVar["SecurityMonitoringSuppressionSort"]
    ENABLED_DESCENDING: ClassVar["SecurityMonitoringSuppressionSort"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringSuppressionSort.NAME = SecurityMonitoringSuppressionSort("name")
SecurityMonitoringSuppressionSort.START_DATE = SecurityMonitoringSuppressionSort("start_date")
SecurityMonitoringSuppressionSort.EXPIRATION_DATE = SecurityMonitoringSuppressionSort("expiration_date")
SecurityMonitoringSuppressionSort.UPDATE_DATE = SecurityMonitoringSuppressionSort("update_date")
SecurityMonitoringSuppressionSort.ENABLED = SecurityMonitoringSuppressionSort("enabled")
SecurityMonitoringSuppressionSort.NAME_DESCENDING = SecurityMonitoringSuppressionSort("-name")
SecurityMonitoringSuppressionSort.START_DATE_DESCENDING = SecurityMonitoringSuppressionSort("-start_date")
SecurityMonitoringSuppressionSort.EXPIRATION_DATE_DESCENDING = SecurityMonitoringSuppressionSort("-expiration_date")
SecurityMonitoringSuppressionSort.UPDATE_DATE_DESCENDING = SecurityMonitoringSuppressionSort("-update_date")
SecurityMonitoringSuppressionSort.CREATION_DATE_DESCENDING = SecurityMonitoringSuppressionSort("-creation_date")
SecurityMonitoringSuppressionSort.ENABLED_DESCENDING = SecurityMonitoringSuppressionSort("-enabled")
