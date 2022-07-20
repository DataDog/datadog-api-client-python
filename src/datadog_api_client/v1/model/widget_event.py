# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WidgetEvent(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "q": (str,),
            "tags_execution": (str,),
        }

    attribute_map = {
        "q": "q",
        "tags_execution": "tags_execution",
    }

    def __init__(self, q, *args, **kwargs):
        """
        Event overlay control options.

        See the dedicated `Events JSON schema documentation <https://docs.datadoghq.com/dashboards/graphing_json/widget_json/#events-schema>`_
        to learn how to build the ``<EVENTS_SCHEMA>``.

        :param q: Query definition.
        :type q: str

        :param tags_execution: The execution method for multi-value filters.
        :type tags_execution: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.q = q

    @classmethod
    def _from_openapi_data(cls, q, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetEvent, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.q = q
        return self
