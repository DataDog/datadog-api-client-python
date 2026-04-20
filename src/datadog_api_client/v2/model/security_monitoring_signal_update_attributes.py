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
    from datadog_api_client.v2.model.security_monitoring_signal_archive_reason import (
        SecurityMonitoringSignalArchiveReason,
    )
    from datadog_api_client.v2.model.security_monitoring_triage_user import SecurityMonitoringTriageUser
    from datadog_api_client.v2.model.security_monitoring_signal_state import SecurityMonitoringSignalState


class SecurityMonitoringSignalUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_archive_reason import (
            SecurityMonitoringSignalArchiveReason,
        )
        from datadog_api_client.v2.model.security_monitoring_triage_user import SecurityMonitoringTriageUser
        from datadog_api_client.v2.model.security_monitoring_signal_state import SecurityMonitoringSignalState

        return {
            "archive_comment": (str,),
            "archive_reason": (SecurityMonitoringSignalArchiveReason,),
            "assignee": (SecurityMonitoringTriageUser,),
            "state": (SecurityMonitoringSignalState,),
            "version": (int,),
        }

    attribute_map = {
        "archive_comment": "archive_comment",
        "archive_reason": "archive_reason",
        "assignee": "assignee",
        "state": "state",
        "version": "version",
    }

    def __init__(
        self_,
        archive_comment: Union[str, UnsetType] = unset,
        archive_reason: Union[SecurityMonitoringSignalArchiveReason, UnsetType] = unset,
        assignee: Union[SecurityMonitoringTriageUser, UnsetType] = unset,
        state: Union[SecurityMonitoringSignalState, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating the triage state or assignee of a security signal.

        :param archive_comment: Optional comment to display on archived signals.
        :type archive_comment: str, optional

        :param archive_reason: Reason a signal is archived.
        :type archive_reason: SecurityMonitoringSignalArchiveReason, optional

        :param assignee: Object representing a given user entity.
        :type assignee: SecurityMonitoringTriageUser, optional

        :param state: The new triage state of the signal.
        :type state: SecurityMonitoringSignalState, optional

        :param version: Version of the updated signal. If server side version is higher, update will be rejected.
        :type version: int, optional
        """
        if archive_comment is not unset:
            kwargs["archive_comment"] = archive_comment
        if archive_reason is not unset:
            kwargs["archive_reason"] = archive_reason
        if assignee is not unset:
            kwargs["assignee"] = assignee
        if state is not unset:
            kwargs["state"] = state
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
