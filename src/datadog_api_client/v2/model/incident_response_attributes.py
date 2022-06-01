# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


class IncidentResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
        from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle

        return {
            "created": (datetime,),
            "customer_impact_duration": (int,),
            "customer_impact_end": (datetime, none_type),
            "customer_impact_scope": (str, none_type),
            "customer_impact_start": (datetime, none_type),
            "customer_impacted": (bool,),
            "detected": (datetime, none_type),
            "fields": ({str: (IncidentFieldAttributes,)},),
            "modified": (datetime,),
            "notification_handles": ([IncidentNotificationHandle], none_type),
            "postmortem_id": (str,),
            "public_id": (int,),
            "resolved": (datetime, none_type),
            "time_to_detect": (int,),
            "time_to_internal_response": (int,),
            "time_to_repair": (int,),
            "time_to_resolve": (int,),
            "title": (str,),
        }

    attribute_map = {
        "created": "created",
        "customer_impact_duration": "customer_impact_duration",
        "customer_impact_end": "customer_impact_end",
        "customer_impact_scope": "customer_impact_scope",
        "customer_impact_start": "customer_impact_start",
        "customer_impacted": "customer_impacted",
        "detected": "detected",
        "fields": "fields",
        "modified": "modified",
        "notification_handles": "notification_handles",
        "postmortem_id": "postmortem_id",
        "public_id": "public_id",
        "resolved": "resolved",
        "time_to_detect": "time_to_detect",
        "time_to_internal_response": "time_to_internal_response",
        "time_to_repair": "time_to_repair",
        "time_to_resolve": "time_to_resolve",
        "title": "title",
    }
    read_only_vars = {
        "created",
        "customer_impact_duration",
        "modified",
        "time_to_detect",
        "time_to_internal_response",
        "time_to_repair",
        "time_to_resolve",
    }

    def __init__(self, title, *args, **kwargs):
        """
        The incident's attributes from a response.

        :param created: Timestamp when the incident was created.
        :type created: datetime, optional

        :param customer_impact_duration: Length of the incident's customer impact in seconds.
            Equals the difference between ``customer_impact_start`` and ``customer_impact_end``.
        :type customer_impact_duration: int, optional

        :param customer_impact_end: Timestamp when customers were no longer impacted by the incident.
        :type customer_impact_end: datetime, none_type, optional

        :param customer_impact_scope: A summary of the impact customers experienced during the incident.
        :type customer_impact_scope: str, none_type, optional

        :param customer_impact_start: Timestamp when customers began being impacted by the incident.
        :type customer_impact_start: datetime, none_type, optional

        :param customer_impacted: A flag indicating whether the incident caused customer impact.
        :type customer_impacted: bool, optional

        :param detected: Timestamp when the incident was detected.
        :type detected: datetime, none_type, optional

        :param fields: A condensed view of the user-defined fields attached to incidents.
        :type fields: {str: (IncidentFieldAttributes,)}, optional

        :param modified: Timestamp when the incident was last modified.
        :type modified: datetime, optional

        :param notification_handles: Notification handles that will be notified of the incident during update.
        :type notification_handles: [IncidentNotificationHandle], none_type, optional

        :param postmortem_id: The UUID of the postmortem object attached to the incident.
        :type postmortem_id: str, optional

        :param public_id: The monotonically increasing integer ID for the incident.
        :type public_id: int, optional

        :param resolved: Timestamp when the incident's state was set to resolved.
        :type resolved: datetime, none_type, optional

        :param time_to_detect: The amount of time in seconds to detect the incident.
            Equals the difference between ``customer_impact_start`` and ``detected``.
        :type time_to_detect: int, optional

        :param time_to_internal_response: The amount of time in seconds to call incident after detection. Equals the difference of ``detected`` and ``created``.
        :type time_to_internal_response: int, optional

        :param time_to_repair: The amount of time in seconds to resolve customer impact after detecting the issue. Equals the difference between ``customer_impact_end`` and ``detected``.
        :type time_to_repair: int, optional

        :param time_to_resolve: The amount of time in seconds to resolve the incident after it was created. Equals the difference between ``created`` and ``resolved``.
        :type time_to_resolve: int, optional

        :param title: The title of the incident, which summarizes what happened.
        :type title: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.title = title

    @classmethod
    def _from_openapi_data(cls, title, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentResponseAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.title = title
        return self
