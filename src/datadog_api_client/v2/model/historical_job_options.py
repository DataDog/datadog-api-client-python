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
    from datadog_api_client.v2.model.security_monitoring_rule_detection_method import (
        SecurityMonitoringRuleDetectionMethod,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_evaluation_window import (
        SecurityMonitoringRuleEvaluationWindow,
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
    from datadog_api_client.v2.model.security_monitoring_rule_third_party_options import (
        SecurityMonitoringRuleThirdPartyOptions,
    )


class HistoricalJobOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_detection_method import (
            SecurityMonitoringRuleDetectionMethod,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_evaluation_window import (
            SecurityMonitoringRuleEvaluationWindow,
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
        from datadog_api_client.v2.model.security_monitoring_rule_third_party_options import (
            SecurityMonitoringRuleThirdPartyOptions,
        )

        return {
            "detection_method": (SecurityMonitoringRuleDetectionMethod,),
            "evaluation_window": (SecurityMonitoringRuleEvaluationWindow,),
            "impossible_travel_options": (SecurityMonitoringRuleImpossibleTravelOptions,),
            "keep_alive": (SecurityMonitoringRuleKeepAlive,),
            "max_signal_duration": (SecurityMonitoringRuleMaxSignalDuration,),
            "new_value_options": (SecurityMonitoringRuleNewValueOptions,),
            "third_party_rule_options": (SecurityMonitoringRuleThirdPartyOptions,),
        }

    attribute_map = {
        "detection_method": "detectionMethod",
        "evaluation_window": "evaluationWindow",
        "impossible_travel_options": "impossibleTravelOptions",
        "keep_alive": "keepAlive",
        "max_signal_duration": "maxSignalDuration",
        "new_value_options": "newValueOptions",
        "third_party_rule_options": "thirdPartyRuleOptions",
    }

    def __init__(
        self_,
        detection_method: Union[SecurityMonitoringRuleDetectionMethod, UnsetType] = unset,
        evaluation_window: Union[SecurityMonitoringRuleEvaluationWindow, UnsetType] = unset,
        impossible_travel_options: Union[SecurityMonitoringRuleImpossibleTravelOptions, UnsetType] = unset,
        keep_alive: Union[SecurityMonitoringRuleKeepAlive, UnsetType] = unset,
        max_signal_duration: Union[SecurityMonitoringRuleMaxSignalDuration, UnsetType] = unset,
        new_value_options: Union[SecurityMonitoringRuleNewValueOptions, UnsetType] = unset,
        third_party_rule_options: Union[SecurityMonitoringRuleThirdPartyOptions, UnsetType] = unset,
        **kwargs,
    ):
        """
        Job options.

        :param detection_method: The detection method.
        :type detection_method: SecurityMonitoringRuleDetectionMethod, optional

        :param evaluation_window: A time window is specified to match when at least one of the cases matches true. This is a sliding window
            and evaluates in real time. For third party detection method, this field is not used.
        :type evaluation_window: SecurityMonitoringRuleEvaluationWindow, optional

        :param impossible_travel_options: Options on impossible travel detection method.
        :type impossible_travel_options: SecurityMonitoringRuleImpossibleTravelOptions, optional

        :param keep_alive: Once a signal is generated, the signal will remain "open" if a case is matched at least once within
            this keep alive window. For third party detection method, this field is not used.
        :type keep_alive: SecurityMonitoringRuleKeepAlive, optional

        :param max_signal_duration: A signal will "close" regardless of the query being matched once the time exceeds the maximum duration.
            This time is calculated from the first seen timestamp.
        :type max_signal_duration: SecurityMonitoringRuleMaxSignalDuration, optional

        :param new_value_options: Options on new value detection method.
        :type new_value_options: SecurityMonitoringRuleNewValueOptions, optional

        :param third_party_rule_options: Options on third party detection method.
        :type third_party_rule_options: SecurityMonitoringRuleThirdPartyOptions, optional
        """
        if detection_method is not unset:
            kwargs["detection_method"] = detection_method
        if evaluation_window is not unset:
            kwargs["evaluation_window"] = evaluation_window
        if impossible_travel_options is not unset:
            kwargs["impossible_travel_options"] = impossible_travel_options
        if keep_alive is not unset:
            kwargs["keep_alive"] = keep_alive
        if max_signal_duration is not unset:
            kwargs["max_signal_duration"] = max_signal_duration
        if new_value_options is not unset:
            kwargs["new_value_options"] = new_value_options
        if third_party_rule_options is not unset:
            kwargs["third_party_rule_options"] = third_party_rule_options
        super().__init__(kwargs)
