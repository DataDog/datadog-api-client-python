# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
        from datadog_api_client.v2.model.incident_timeline_cell_create_attributes import (
            IncidentTimelineCellCreateAttributes,
        )
        from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle

        return {
            "customer_impacted": (bool,),
            "fields": ({str: (IncidentFieldAttributes,)},),
            "initial_cells": ([IncidentTimelineCellCreateAttributes],),
            "notification_handles": ([IncidentNotificationHandle],),
            "title": (str,),
        }

    attribute_map = {
        "customer_impacted": "customer_impacted",
        "fields": "fields",
        "initial_cells": "initial_cells",
        "notification_handles": "notification_handles",
        "title": "title",
    }

    def __init__(self, customer_impacted, title, *args, **kwargs):
        """
        The incident's attributes for a create request.

        :param customer_impacted: A flag indicating whether the incident caused customer impact.
        :type customer_impacted: bool

        :param fields: A condensed view of the user-defined fields for which to create initial selections.
        :type fields: {str: (IncidentFieldAttributes,)}, optional

        :param initial_cells: An array of initial timeline cells to be placed at the beginning of the incident timeline.
        :type initial_cells: [IncidentTimelineCellCreateAttributes], optional

        :param notification_handles: Notification handles that will be notified of the incident at creation.
        :type notification_handles: [IncidentNotificationHandle], optional

        :param title: The title of the incident, which summarizes what happened.
        :type title: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.customer_impacted = customer_impacted
        self.title = title

    @classmethod
    def _from_openapi_data(cls, customer_impacted, title, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.customer_impacted = customer_impacted
        self.title = title
        return self
