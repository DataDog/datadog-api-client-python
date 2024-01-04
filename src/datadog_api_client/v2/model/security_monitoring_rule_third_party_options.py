# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
    from datadog_api_client.v2.model.security_monitoring_third_party_root_query import (
        SecurityMonitoringThirdPartyRootQuery,
    )


class SecurityMonitoringRuleThirdPartyOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
        from datadog_api_client.v2.model.security_monitoring_third_party_root_query import (
            SecurityMonitoringThirdPartyRootQuery,
        )

        return {
            "default_notifications": ([str],),
            "default_status": (SecurityMonitoringRuleSeverity,),
            "root_queries": ([SecurityMonitoringThirdPartyRootQuery],),
            "signal_title_template": (str,),
        }

    attribute_map = {
        "default_notifications": "defaultNotifications",
        "default_status": "defaultStatus",
        "root_queries": "rootQueries",
        "signal_title_template": "signalTitleTemplate",
    }

    def __init__(
        self_,
        default_notifications: Union[List[str], UnsetType] = unset,
        default_status: Union[SecurityMonitoringRuleSeverity, UnsetType] = unset,
        root_queries: Union[List[SecurityMonitoringThirdPartyRootQuery], UnsetType] = unset,
        signal_title_template: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Options on third party rules.

        :param default_notifications: Notification targets for the logs that do not correspond to any of the cases.
        :type default_notifications: [str], optional

        :param default_status: Severity of the Security Signal.
        :type default_status: SecurityMonitoringRuleSeverity, optional

        :param root_queries: Queries to be combined with third party case queries. Each of them can have different group by fields, to aggregate differently based on the type of alert.
        :type root_queries: [SecurityMonitoringThirdPartyRootQuery], optional

        :param signal_title_template: A template for the signal title; if omitted, the title is generated based on the case name.
        :type signal_title_template: str, optional
        """
        if default_notifications is not unset:
            kwargs["default_notifications"] = default_notifications
        if default_status is not unset:
            kwargs["default_status"] = default_status
        if root_queries is not unset:
            kwargs["root_queries"] = root_queries
        if signal_title_template is not unset:
            kwargs["signal_title_template"] = signal_title_template
        super().__init__(kwargs)
