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


class SecurityMonitoringThirdPartyRuleCaseCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity

        return {
            "name": (str,),
            "notifications": ([str],),
            "query": (str,),
            "status": (SecurityMonitoringRuleSeverity,),
        }

    attribute_map = {
        "name": "name",
        "notifications": "notifications",
        "query": "query",
        "status": "status",
    }

    def __init__(
        self_,
        status: SecurityMonitoringRuleSeverity,
        name: Union[str, UnsetType] = unset,
        notifications: Union[List[str], UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Case when a signal is generated by a third party rule.

        :param name: Name of the case.
        :type name: str, optional

        :param notifications: Notification targets for each rule case.
        :type notifications: [str], optional

        :param query: A query to map a third party event to this case.
        :type query: str, optional

        :param status: Severity of the Security Signal.
        :type status: SecurityMonitoringRuleSeverity
        """
        if name is not unset:
            kwargs["name"] = name
        if notifications is not unset:
            kwargs["notifications"] = notifications
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)

        self_.status = status
