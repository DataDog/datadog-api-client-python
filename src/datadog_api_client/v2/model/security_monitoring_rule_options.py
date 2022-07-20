# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringRuleOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_detection_method import (
            SecurityMonitoringRuleDetectionMethod,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_evaluation_window import (
            SecurityMonitoringRuleEvaluationWindow,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_hardcoded_evaluator_type import (
            SecurityMonitoringRuleHardcodedEvaluatorType,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_impossible_travel_options import (
            SecurityMonitoringRuleImpossibleTravelOptions,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_keep_alive import SecurityMonitoringRuleKeepAlive
        from datadog_api_client.v2.model.security_monitoring_rule_max_signal_duration import (
            SecurityMonitoringRuleMaxSignalDuration,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_new_value_options import (
            SecurityMonitoringRuleNewValueOptions,
        )

        return {
            "decrease_criticality_based_on_env": (bool,),
            "detection_method": (SecurityMonitoringRuleDetectionMethod,),
            "evaluation_window": (SecurityMonitoringRuleEvaluationWindow,),
            "hardcoded_evaluator_type": (SecurityMonitoringRuleHardcodedEvaluatorType,),
            "impossible_travel_options": (SecurityMonitoringRuleImpossibleTravelOptions,),
            "keep_alive": (SecurityMonitoringRuleKeepAlive,),
            "max_signal_duration": (SecurityMonitoringRuleMaxSignalDuration,),
            "new_value_options": (SecurityMonitoringRuleNewValueOptions,),
        }

    attribute_map = {
        "decrease_criticality_based_on_env": "decreaseCriticalityBasedOnEnv",
        "detection_method": "detectionMethod",
        "evaluation_window": "evaluationWindow",
        "hardcoded_evaluator_type": "hardcodedEvaluatorType",
        "impossible_travel_options": "impossibleTravelOptions",
        "keep_alive": "keepAlive",
        "max_signal_duration": "maxSignalDuration",
        "new_value_options": "newValueOptions",
    }

    def __init__(self, *args, **kwargs):
        """
        Options on rules.

        :param decrease_criticality_based_on_env: If true, signals in non-production environments have a lower severity than what is defined by the rule case, which can reduce signal noise.
            The severity is decreased by one level: ``CRITICAL`` in production becomes ``HIGH`` in non-production, ``HIGH`` becomes ``MEDIUM`` and so on. ``INFO`` remains ``INFO``.
            The decrement is applied when the environment tag of the signal starts with ``staging`` , ``test`` or ``dev``.
        :type decrease_criticality_based_on_env: bool, optional

        :param detection_method: The detection method.
        :type detection_method: SecurityMonitoringRuleDetectionMethod, optional

        :param evaluation_window: A time window is specified to match when at least one of the cases matches true. This is a sliding window
            and evaluates in real time.
        :type evaluation_window: SecurityMonitoringRuleEvaluationWindow, optional

        :param hardcoded_evaluator_type: Hardcoded evaluator type.
        :type hardcoded_evaluator_type: SecurityMonitoringRuleHardcodedEvaluatorType, optional

        :param impossible_travel_options: Options on impossible travel rules.
        :type impossible_travel_options: SecurityMonitoringRuleImpossibleTravelOptions, optional

        :param keep_alive: Once a signal is generated, the signal will remain “open” if a case is matched at least once within
            this keep alive window.
        :type keep_alive: SecurityMonitoringRuleKeepAlive, optional

        :param max_signal_duration: A signal will “close” regardless of the query being matched once the time exceeds the maximum duration.
            This time is calculated from the first seen timestamp.
        :type max_signal_duration: SecurityMonitoringRuleMaxSignalDuration, optional

        :param new_value_options: Options on new value rules.
        :type new_value_options: SecurityMonitoringRuleNewValueOptions, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringRuleOptions, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
