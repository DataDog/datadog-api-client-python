# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity


class ConvertJobResultsToSignalsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity

        return {
            "job_result_ids": ([str],),
            "notifications": ([str],),
            "signal_message": (str,),
            "signal_severity": (SecurityMonitoringRuleSeverity,),
        }

    attribute_map = {
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
        **kwargs,
    ):
        """
        Attributes for converting historical job results to signals.

        :param job_result_ids: Job result IDs.
        :type job_result_ids: [str]

        :param notifications: Notifications sent.
        :type notifications: [str]

        :param signal_message: Message of generated signals.
        :type signal_message: str

        :param signal_severity: Severity of the Security Signal.
        :type signal_severity: SecurityMonitoringRuleSeverity
        """
        super().__init__(kwargs)

        self_.job_result_ids = job_result_ids
        self_.notifications = notifications
        self_.signal_message = signal_message
        self_.signal_severity = signal_severity
