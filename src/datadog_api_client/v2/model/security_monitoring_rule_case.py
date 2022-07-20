# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringRuleCase(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity

        return {
            "condition": (str,),
            "name": (str,),
            "notifications": ([str],),
            "status": (SecurityMonitoringRuleSeverity,),
        }

    attribute_map = {
        "condition": "condition",
        "name": "name",
        "notifications": "notifications",
        "status": "status",
    }

    def __init__(self, *args, **kwargs):
        """
        Case when signal is generated.

        :param condition: A rule case contains logical operations ( ``>`` , ``>=`` , ``&&`` , ``||`` ) to determine if a signal should be generated
            based on the event counts in the previously defined queries.
        :type condition: str, optional

        :param name: Name of the case.
        :type name: str, optional

        :param notifications: Notification targets for each rule case.
        :type notifications: [str], optional

        :param status: Severity of the Security Signal.
        :type status: SecurityMonitoringRuleSeverity, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringRuleCase, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
