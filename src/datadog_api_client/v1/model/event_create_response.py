# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class EventCreateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.event import Event

        return {
            "event": (Event,),
            "status": (str,),
        }

    attribute_map = {
        "event": "event",
        "status": "status",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing an event response.

        :param event: Object representing an event.
        :type event: Event, optional

        :param status: A status.
        :type status: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(EventCreateResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
