# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_rule_anomaly_detection_options_bucket_duration import (
        SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_anomaly_detection_options_detection_tolerance import (
        SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_anomaly_detection_options_learning_duration import (
        SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration,
    )


class SecurityMonitoringRuleAnomalyDetectionOptions(ModelNormal):
    validations = {
        "learning_period_baseline": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_anomaly_detection_options_bucket_duration import (
            SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_anomaly_detection_options_detection_tolerance import (
            SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_anomaly_detection_options_learning_duration import (
            SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration,
        )

        return {
            "bucket_duration": (SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration,),
            "detection_tolerance": (SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance,),
            "learning_duration": (SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration,),
            "learning_period_baseline": (int,),
        }

    attribute_map = {
        "bucket_duration": "bucketDuration",
        "detection_tolerance": "detectionTolerance",
        "learning_duration": "learningDuration",
        "learning_period_baseline": "learningPeriodBaseline",
    }

    def __init__(
        self_,
        bucket_duration: Union[SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration, UnsetType] = unset,
        detection_tolerance: Union[SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance, UnsetType] = unset,
        learning_duration: Union[SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration, UnsetType] = unset,
        learning_period_baseline: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Options on anomaly detection method.

        :param bucket_duration: Duration in seconds of the time buckets used to aggregate events matched by the rule.
            Must be greater than or equal to 300.
        :type bucket_duration: SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration, optional

        :param detection_tolerance: An optional parameter that sets how permissive anomaly detection is.
            Higher values require higher deviations before triggering a signal.
        :type detection_tolerance: SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance, optional

        :param learning_duration: Learning duration in hours. Anomaly detection waits for at least this amount of historical data before it starts evaluating.
        :type learning_duration: SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration, optional

        :param learning_period_baseline: An optional override baseline to apply while the rule is in the learning period. Must be greater than or equal to 0.
        :type learning_period_baseline: int, optional
        """
        if bucket_duration is not unset:
            kwargs["bucket_duration"] = bucket_duration
        if detection_tolerance is not unset:
            kwargs["detection_tolerance"] = detection_tolerance
        if learning_duration is not unset:
            kwargs["learning_duration"] = learning_duration
        if learning_period_baseline is not unset:
            kwargs["learning_period_baseline"] = learning_period_baseline
        super().__init__(kwargs)
