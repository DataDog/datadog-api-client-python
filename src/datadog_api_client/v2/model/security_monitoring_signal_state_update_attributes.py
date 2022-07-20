# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalStateUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_archive_reason import (
            SecurityMonitoringSignalArchiveReason,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_state import SecurityMonitoringSignalState

        return {
            "archive_comment": (str,),
            "archive_reason": (SecurityMonitoringSignalArchiveReason,),
            "state": (SecurityMonitoringSignalState,),
            "version": (int,),
        }

    attribute_map = {
        "archive_comment": "archive_comment",
        "archive_reason": "archive_reason",
        "state": "state",
        "version": "version",
    }

    def __init__(self, state, *args, **kwargs):
        """
        Attributes describing the change of state of a security signal.

        :param archive_comment: Optional comment to display on archived signals.
        :type archive_comment: str, optional

        :param archive_reason: Reason a signal is archived.
        :type archive_reason: SecurityMonitoringSignalArchiveReason, optional

        :param state: The new triage state of the signal.
        :type state: SecurityMonitoringSignalState

        :param version: Version of the updated signal. If server side version is higher, update will be rejected.
        :type version: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.state = state

    @classmethod
    def _from_openapi_data(cls, state, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringSignalStateUpdateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.state = state
        return self
