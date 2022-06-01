# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignal(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_attributes import SecurityMonitoringSignalAttributes
        from datadog_api_client.v2.model.security_monitoring_signal_type import SecurityMonitoringSignalType

        return {
            "attributes": (SecurityMonitoringSignalAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringSignalType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Object description of a security signal.

        :param attributes: The object containing all signal attributes and their
            associated values.
        :type attributes: SecurityMonitoringSignalAttributes, optional

        :param id: The unique ID of the security signal.
        :type id: str, optional

        :param type: The type of event.
        :type type: SecurityMonitoringSignalType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringSignal, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
