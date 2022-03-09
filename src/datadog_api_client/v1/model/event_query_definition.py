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
            "tags_execution": (str,),
        }

    attribute_map = {
        "search": "search",
        "tags_execution": "tags_execution",
    }

    def __init__(self, search, tags_execution, *args, **kwargs):
        """
        The event query.

        :param search: The query being made on the event.
        :type search: str

        :param tags_execution: The execution method for multi-value filters. Can be either and or or.
        :type tags_execution: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.search = search
        self.tags_execution = tags_execution

    @classmethod
    def _from_openapi_data(cls, search, tags_execution, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(EventQueryDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.search = search
        self.tags_execution = tags_execution
        return self
