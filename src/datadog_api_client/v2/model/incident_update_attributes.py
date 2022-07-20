# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


class IncidentUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
        from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle

        return {
            "customer_impact_end": (datetime, none_type),
            "customer_impact_scope": (str,),
            "customer_impact_start": (datetime, none_type),
            "customer_impacted": (bool,),
            "detected": (datetime, none_type),
            "fields": ({str: (IncidentFieldAttributes,)},),
            "notification_handles": ([IncidentNotificationHandle],),
            "resolved": (datetime, none_type),
            "title": (str,),
        }

    attribute_map = {
        "customer_impact_end": "customer_impact_end",
        "customer_impact_scope": "customer_impact_scope",
        "customer_impact_start": "customer_impact_start",
        "customer_impacted": "customer_impacted",
        "detected": "detected",
        "fields": "fields",
        "notification_handles": "notification_handles",
        "resolved": "resolved",
        "title": "title",
    }

    def __init__(self, *args, **kwargs):
        """
        The incident's attributes for an update request.

        :param customer_impact_end: Timestamp when customers were no longer impacted by the incident.
        :type customer_impact_end: datetime, none_type, optional

        :param customer_impact_scope: A summary of the impact customers experienced during the incident.
        :type customer_impact_scope: str, optional

        :param customer_impact_start: Timestamp when customers began being impacted by the incident.
        :type customer_impact_start: datetime, none_type, optional

        :param customer_impacted: A flag indicating whether the incident caused customer impact.
        :type customer_impacted: bool, optional

        :param detected: Timestamp when the incident was detected.
        :type detected: datetime, none_type, optional

        :param fields: A condensed view of the user-defined fields for which to update selections.
        :type fields: {str: (IncidentFieldAttributes,)}, optional

        :param notification_handles: Notification handles that will be notified of the incident during update.
        :type notification_handles: [IncidentNotificationHandle], optional

        :param resolved: Timestamp when the incident's state was set to resolved.
        :type resolved: datetime, none_type, optional

        :param title: The title of the incident, which summarizes what happened.
        :type title: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentUpdateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
