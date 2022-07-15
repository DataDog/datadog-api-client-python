# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalIncidentsUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_incidents_update_attributes import (
            SecurityMonitoringSignalIncidentsUpdateAttributes,
        )

        return {
            "attributes": (SecurityMonitoringSignalIncidentsUpdateAttributes,),
        }

    attribute_map = {
        "attributes": "attributes",
    }

    def __init__(self, attributes, *args, **kwargs):
        """
        Data containing the patch for changing the related incidents of a signal.

        :param attributes: Attributes describing the new list of related signals for a security signal.
        :type attributes: SecurityMonitoringSignalIncidentsUpdateAttributes
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes

    @classmethod
    def _from_openapi_data(cls, attributes, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringSignalIncidentsUpdateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        return self
