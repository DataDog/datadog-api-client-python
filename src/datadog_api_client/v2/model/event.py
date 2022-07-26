# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class Event(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "name": (str,),
            "source_id": (int,),
            "type": (str,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "source_id": "source_id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        The metadata associated with a request.

        :param id: Event ID.
        :type id: str, optional

        :param name: The event name.
        :type name: str, optional

        :param source_id: Event source ID.
        :type source_id: int, optional

        :param type: Event type.
        :type type: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(Event, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
