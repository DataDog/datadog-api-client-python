# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalIncidentsUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_incident_ids import (
            SecurityMonitoringSignalIncidentIds,
        )

        return {
            "incident_ids": (SecurityMonitoringSignalIncidentIds,),
            "version": (int,),
        }

    attribute_map = {
        "incident_ids": "incident_ids",
        "version": "version",
    }

    def __init__(self, incident_ids, *args, **kwargs):
        """
        Attributes describing the new list of related signals for a security signal.

        :param incident_ids: Array of incidents that are associated with this signal.
        :type incident_ids: SecurityMonitoringSignalIncidentIds

        :param version: Version of the updated signal. If server side version is higher, update will be rejected.
        :type version: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.incident_ids = incident_ids

    @classmethod
    def _from_openapi_data(cls, incident_ids, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringSignalIncidentsUpdateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.incident_ids = incident_ids
        return self
