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


class ConvertJobResultsToSignalsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity

        return {
            "id": (str,),
            "job_result_ids": ([str],),
            "notifications": ([str],),
            "signal_message": (str,),
            "signal_severity": (SecurityMonitoringRuleSeverity,),
        }

    attribute_map = {
        "id": "id",
        "job_result_ids": "jobResultIds",
        "notifications": "notifications",
        "signal_message": "signalMessage",
        "signal_severity": "signalSeverity",
    }

    def __init__(
        self_,
        job_result_ids: List[str],
        notifications: List[str],
        signal_message: str,
        signal_severity: SecurityMonitoringRuleSeverity,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for converting historical job results to signals.

        :param id: Request ID.
        :type id: str, optional

        :param job_result_ids: Job result IDs.
        :type job_result_ids: [str]

        :param notifications: Notifications sent.
        :type notifications: [str]

        :param signal_message: Message of generated signals.
        :type signal_message: str

        :param signal_severity: Severity of the Security Signal.
        :type signal_severity: SecurityMonitoringRuleSeverity
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.job_result_ids = job_result_ids
        self_.notifications = notifications
        self_.signal_message = signal_message
        self_.signal_severity = signal_severity
