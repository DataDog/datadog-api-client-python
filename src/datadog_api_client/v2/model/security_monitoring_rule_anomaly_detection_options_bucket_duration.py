# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration(ModelSimple):
    """
    Duration in seconds of the time buckets used to aggregate events matched by the rule.
        Must be greater than or equal to 300.

    :param value: Must be one of [300, 600, 900, 1800, 3600, 10800].
    :type value: int
    """

    allowed_values = {
        300,
        600,
        900,
        1800,
        3600,
        10800,
    }
    FIVE_MINUTES: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration"]
    TEN_MINUTES: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration"]
    FIFTEEN_MINUTES: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration"]
    THIRTY_MINUTES: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration"]
    ONE_HOUR: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration"]
    THREE_HOURS: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }


SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration.FIVE_MINUTES = (
    SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration(300)
)
SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration.TEN_MINUTES = (
    SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration(600)
)
SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration.FIFTEEN_MINUTES = (
    SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration(900)
)
SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration.THIRTY_MINUTES = (
    SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration(1800)
)
SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration.ONE_HOUR = (
    SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration(3600)
)
SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration.THREE_HOURS = (
    SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration(10800)
)
