# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class EventsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_response import EventResponse
        from datadog_api_client.v2.model.events_list_response_links import EventsListResponseLinks
        from datadog_api_client.v2.model.events_response_metadata import EventsResponseMetadata

        return {
            "data": ([EventResponse],),
            "links": (EventsListResponseLinks,),
            "meta": (EventsResponseMetadata,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(self, *args, **kwargs):
        """
        The response object with all events matching the request and pagination information.

        :param data: An array of events matching the request.
        :type data: [EventResponse], optional

        :param links: Links attributes.
        :type links: EventsListResponseLinks, optional

        :param meta: The metadata associated with a request.
        :type meta: EventsResponseMetadata, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(EventsListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
