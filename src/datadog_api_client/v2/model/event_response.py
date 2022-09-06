# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class EventResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_response_attributes import EventResponseAttributes
        from datadog_api_client.v2.model.event_type import EventType

        return {
            "attributes": (EventResponseAttributes,),
            "id": (str,),
            "type": (EventType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, *args, **kwargs):
        """
        The object description of an event after being processed and stored by Datadog.

        :param attributes: The object description of an event response attribute.
        :type attributes: EventResponseAttributes, optional

        :param id: the unique ID of the event.
        :type id: str, optional

        :param type: Type of the event.
        :type type: EventType, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
