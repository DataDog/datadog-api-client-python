# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration(ModelSimple):
    """
    Learning duration in hours. Anomaly detection waits for at least this amount of historical data before it starts evaluating.

    :param value: Must be one of [1, 6, 12, 24, 48, 168, 336].
    :type value: int
    """

    allowed_values = {
        1,
        6,
        12,
        24,
        48,
        168,
        336,
    }
    ONE_HOUR: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration"]
    SIX_HOURS: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration"]
    TWELVE_HOURS: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration"]
    ONE_DAY: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration"]
    TWO_DAYS: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration"]
    ONE_WEEK: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration"]
    TWO_WEEKS: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }


SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration.ONE_HOUR = (
    SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration(1)
)
SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration.SIX_HOURS = (
    SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration(6)
)
SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration.TWELVE_HOURS = (
    SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration(12)
)
SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration.ONE_DAY = (
    SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration(24)
)
SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration.TWO_DAYS = (
    SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration(48)
)
SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration.ONE_WEEK = (
    SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration(168)
)
SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration.TWO_WEEKS = (
    SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration(336)
)
