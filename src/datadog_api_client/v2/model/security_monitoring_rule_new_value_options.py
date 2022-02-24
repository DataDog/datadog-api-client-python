# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.security_monitoring_rule_new_value_options_forget_after import (
        SecurityMonitoringRuleNewValueOptionsForgetAfter,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_new_value_options_learning_duration import (
        SecurityMonitoringRuleNewValueOptionsLearningDuration,
    )

    globals()["SecurityMonitoringRuleNewValueOptionsForgetAfter"] = SecurityMonitoringRuleNewValueOptionsForgetAfter
    globals()[
        "SecurityMonitoringRuleNewValueOptionsLearningDuration"
    ] = SecurityMonitoringRuleNewValueOptionsLearningDuration


class SecurityMonitoringRuleNewValueOptions(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "forget_after": (SecurityMonitoringRuleNewValueOptionsForgetAfter,),
            "learning_duration": (SecurityMonitoringRuleNewValueOptionsLearningDuration,),
        }

    attribute_map = {
        "forget_after": "forgetAfter",
        "learning_duration": "learningDuration",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Options on new value rules.

        :param forget_after: The duration in days after which a learned value is forgotten.
        :type forget_after: SecurityMonitoringRuleNewValueOptionsForgetAfter, optional

        :param learning_duration: The duration in days during which values are learned, and after which signals will be generated for values that
            weren't learned. If set to 0, a signal will be generated for all new values after the first value is learned.
        :type learning_duration: SecurityMonitoringRuleNewValueOptionsLearningDuration, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringRuleNewValueOptions, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
