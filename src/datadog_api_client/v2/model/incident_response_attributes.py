# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
    from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle

    globals()["IncidentFieldAttributes"] = IncidentFieldAttributes
    globals()["IncidentNotificationHandle"] = IncidentNotificationHandle


class IncidentResponseAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "created": (datetime,),
            "customer_impact_duration": (int,),
            "customer_impact_end": (
                datetime,
                none_type,
            ),
            "customer_impact_scope": (
                str,
                none_type,
            ),
            "customer_impact_start": (
                datetime,
                none_type,
            ),
            "customer_impacted": (bool,),
            "detected": (
                datetime,
                none_type,
            ),
            "fields": ({str: (IncidentFieldAttributes,)},),
            "modified": (datetime,),
            "notification_handles": (
                [IncidentNotificationHandle],
                none_type,
            ),
            "postmortem_id": (str,),
            "public_id": (int,),
            "resolved": (
                datetime,
                none_type,
            ),
            "time_to_detect": (int,),
            "time_to_internal_response": (int,),
            "time_to_repair": (int,),
            "time_to_resolve": (int,),
            "title": (str,),
        }

    attribute_map = {
        "title": "title",
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
        """IncidentResponseAttributes - a model defined in OpenAPI

        Args:
            title (str): The title of the incident, which summarizes what happened.

        Keyword Args:
            created (datetime): [optional] Timestamp when the incident was created.
            customer_impact_duration (int): [optional] Length of the incident's customer impact in seconds. Equals the difference between `customer_impact_start` and `customer_impact_end`.
            customer_impact_end (datetime, none_type): [optional] Timestamp when customers were no longer impacted by the incident.
            customer_impact_scope (str, none_type): [optional] A summary of the impact customers experienced during the incident.
            customer_impact_start (datetime, none_type): [optional] Timestamp when customers began being impacted by the incident.
            customer_impacted (bool): [optional] A flag indicating whether the incident caused customer impact.
            detected (datetime, none_type): [optional] Timestamp when the incident was detected.
            fields ({str: (IncidentFieldAttributes,)}): [optional] A condensed view of the user-defined fields attached to incidents.
            modified (datetime): [optional] Timestamp when the incident was last modified.
            notification_handles ([IncidentNotificationHandle], none_type): [optional] Notification handles that will be notified of the incident during update.
            postmortem_id (str): [optional] The UUID of the postmortem object attached to the incident.
            public_id (int): [optional] The monotonically increasing integer ID for the incident.
            resolved (datetime, none_type): [optional] Timestamp when the incident's state was set to resolved.
            time_to_detect (int): [optional] The amount of time in seconds to detect the incident. Equals the difference between `customer_impact_start` and `detected`.
            time_to_internal_response (int): [optional] The amount of time in seconds to call incident after detection. Equals the difference of `detected` and `created`.
            time_to_repair (int): [optional] The amount of time in seconds to resolve customer impact after detecting the issue. Equals the difference between `customer_impact_end` and `detected`.
            time_to_resolve (int): [optional] The amount of time in seconds to resolve the incident after it was created. Equals the difference between `created` and `resolved`.
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
