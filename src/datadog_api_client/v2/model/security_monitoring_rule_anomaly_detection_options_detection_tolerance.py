# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance(ModelSimple):
    """
    An optional parameter that sets how permissive anomaly detection is.
        Higher values require higher deviations before triggering a signal.

    :param value: Must be one of [1, 2, 3, 4, 5].
    :type value: int
    """

    allowed_values = {
        1,
        2,
        3,
        4,
        5,
    }
    ONE: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance"]
    TWO: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance"]
    THREE: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance"]
    FOUR: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance"]
    FIVE: ClassVar["SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }


SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance.ONE = (
    SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance(1)
)
SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance.TWO = (
    SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance(2)
)
SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance.THREE = (
    SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance(3)
)
SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance.FOUR = (
    SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance(4)
)
SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance.FIVE = (
    SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance(5)
)
