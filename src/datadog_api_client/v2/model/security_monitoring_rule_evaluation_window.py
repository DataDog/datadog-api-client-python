# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleEvaluationWindow(ModelSimple):
    """
    A time window is specified to match when at least one of the cases matches true. This is a sliding window
        and evaluates in real time. For third party detection method, this field is not used.

    :param value: Must be one of [0, 60, 300, 600, 900, 1800, 3600, 7200, 10800, 21600, 43200, 86400].
    :type value: int
    """

    allowed_values = {
        0,
        60,
        300,
        600,
        900,
        1800,
        3600,
        7200,
        10800,
        21600,
        43200,
        86400,
    }
    ZERO_MINUTES: ClassVar["SecurityMonitoringRuleEvaluationWindow"]
    ONE_MINUTE: ClassVar["SecurityMonitoringRuleEvaluationWindow"]
    FIVE_MINUTES: ClassVar["SecurityMonitoringRuleEvaluationWindow"]
    TEN_MINUTES: ClassVar["SecurityMonitoringRuleEvaluationWindow"]
    FIFTEEN_MINUTES: ClassVar["SecurityMonitoringRuleEvaluationWindow"]
    THIRTY_MINUTES: ClassVar["SecurityMonitoringRuleEvaluationWindow"]
    ONE_HOUR: ClassVar["SecurityMonitoringRuleEvaluationWindow"]
    TWO_HOURS: ClassVar["SecurityMonitoringRuleEvaluationWindow"]
    THREE_HOURS: ClassVar["SecurityMonitoringRuleEvaluationWindow"]
    SIX_HOURS: ClassVar["SecurityMonitoringRuleEvaluationWindow"]
    TWELVE_HOURS: ClassVar["SecurityMonitoringRuleEvaluationWindow"]
    ONE_DAY: ClassVar["SecurityMonitoringRuleEvaluationWindow"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }


SecurityMonitoringRuleEvaluationWindow.ZERO_MINUTES = SecurityMonitoringRuleEvaluationWindow(0)
SecurityMonitoringRuleEvaluationWindow.ONE_MINUTE = SecurityMonitoringRuleEvaluationWindow(60)
SecurityMonitoringRuleEvaluationWindow.FIVE_MINUTES = SecurityMonitoringRuleEvaluationWindow(300)
SecurityMonitoringRuleEvaluationWindow.TEN_MINUTES = SecurityMonitoringRuleEvaluationWindow(600)
SecurityMonitoringRuleEvaluationWindow.FIFTEEN_MINUTES = SecurityMonitoringRuleEvaluationWindow(900)
SecurityMonitoringRuleEvaluationWindow.THIRTY_MINUTES = SecurityMonitoringRuleEvaluationWindow(1800)
SecurityMonitoringRuleEvaluationWindow.ONE_HOUR = SecurityMonitoringRuleEvaluationWindow(3600)
SecurityMonitoringRuleEvaluationWindow.TWO_HOURS = SecurityMonitoringRuleEvaluationWindow(7200)
SecurityMonitoringRuleEvaluationWindow.THREE_HOURS = SecurityMonitoringRuleEvaluationWindow(10800)
SecurityMonitoringRuleEvaluationWindow.SIX_HOURS = SecurityMonitoringRuleEvaluationWindow(21600)
SecurityMonitoringRuleEvaluationWindow.TWELVE_HOURS = SecurityMonitoringRuleEvaluationWindow(43200)
SecurityMonitoringRuleEvaluationWindow.ONE_DAY = SecurityMonitoringRuleEvaluationWindow(86400)
