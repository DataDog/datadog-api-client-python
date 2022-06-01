# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class EventQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "search": (str,),
        }

    attribute_map = {
        "search": "search",
    }

    def __init__(self, search, *args, **kwargs):
        """
        The event query.

        :param search: The query being made on the event.
        :type search: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.search = search

    @classmethod
    def _from_openapi_data(cls, search, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(EventQueryDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.search = search
        return self
