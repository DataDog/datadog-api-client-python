# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AddSignalToIncidentRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "add_to_signal_timeline": (bool,),
            "incident_id": (int,),
            "version": (int,),
        }

    attribute_map = {
        "add_to_signal_timeline": "add_to_signal_timeline",
        "incident_id": "incident_id",
        "version": "version",
    }

    def __init__(self, incident_id, *args, **kwargs):
        """
        Attributes describing which incident to add the signal to.

        :param add_to_signal_timeline: Whether to post the signal on the incident timeline.
        :type add_to_signal_timeline: bool, optional

        :param incident_id: Public ID attribute of the incident to which the signal will be added.
        :type incident_id: int

        :param version: Version of the updated signal. If server side version is higher, update will be rejected.
        :type version: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.incident_id = incident_id

    @classmethod
    def _from_openapi_data(cls, incident_id, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AddSignalToIncidentRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.incident_id = incident_id
        return self
