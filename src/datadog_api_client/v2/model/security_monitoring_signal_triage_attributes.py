# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalTriageAttributes(ModelNormal):
    validations = {
        "archive_comment_timestamp": {
            "inclusive_minimum": 0,
        },
        "state_update_timestamp": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_triage_user import SecurityMonitoringTriageUser
        from datadog_api_client.v2.model.security_monitoring_signal_archive_reason import (
            SecurityMonitoringSignalArchiveReason,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_incident_ids import (
            SecurityMonitoringSignalIncidentIds,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_state import SecurityMonitoringSignalState

        return {
            "archive_comment": (str,),
            "archive_comment_timestamp": (int,),
            "archive_comment_user": (SecurityMonitoringTriageUser,),
            "archive_reason": (SecurityMonitoringSignalArchiveReason,),
            "assignee": (SecurityMonitoringTriageUser,),
            "incident_ids": (SecurityMonitoringSignalIncidentIds,),
            "state": (SecurityMonitoringSignalState,),
            "state_update_timestamp": (int,),
            "state_update_user": (SecurityMonitoringTriageUser,),
        }

    attribute_map = {
        "archive_comment": "archive_comment",
        "archive_comment_timestamp": "archive_comment_timestamp",
        "archive_comment_user": "archive_comment_user",
        "archive_reason": "archive_reason",
        "assignee": "assignee",
        "incident_ids": "incident_ids",
        "state": "state",
        "state_update_timestamp": "state_update_timestamp",
        "state_update_user": "state_update_user",
    }

    def __init__(self, assignee, incident_ids, state, *args, **kwargs):
        """
        Attributes describing a triage state update operation over a security signal.

        :param archive_comment: Optional comment to display on archived signals.
        :type archive_comment: str, optional

        :param archive_comment_timestamp: Timestamp of the last edit to the comment.
        :type archive_comment_timestamp: int, optional

        :param archive_comment_user: Object representing a given user entity.
        :type archive_comment_user: SecurityMonitoringTriageUser, optional

        :param archive_reason: Reason a signal is archived.
        :type archive_reason: SecurityMonitoringSignalArchiveReason, optional

        :param assignee: Object representing a given user entity.
        :type assignee: SecurityMonitoringTriageUser

        :param incident_ids: Array of incidents that are associated with this signal.
        :type incident_ids: SecurityMonitoringSignalIncidentIds

        :param state: The new triage state of the signal.
        :type state: SecurityMonitoringSignalState

        :param state_update_timestamp: Timestamp of the last update to the signal state.
        :type state_update_timestamp: int, optional

        :param state_update_user: Object representing a given user entity.
        :type state_update_user: SecurityMonitoringTriageUser, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.assignee = assignee
        self.incident_ids = incident_ids
        self.state = state

    @classmethod
    def _from_openapi_data(cls, assignee, incident_ids, state, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringSignalTriageAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.assignee = assignee
        self.incident_ids = incident_ids
        self.state = state
        return self
