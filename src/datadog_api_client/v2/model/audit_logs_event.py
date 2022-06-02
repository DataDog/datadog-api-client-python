# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuditLogsEvent(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.audit_logs_event_attributes import AuditLogsEventAttributes
        from datadog_api_client.v2.model.audit_logs_event_type import AuditLogsEventType

        return {
            "attributes": (AuditLogsEventAttributes,),
            "id": (str,),
            "type": (AuditLogsEventType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Object description of an Audit Logs event after it is processed and stored by Datadog.

        :param attributes: JSON object containing all event attributes and their associated values.
        :type attributes: AuditLogsEventAttributes, optional

        :param id: Unique ID of the event.
        :type id: str, optional

        :param type: Type of the event.
        :type type: AuditLogsEventType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuditLogsEvent, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
