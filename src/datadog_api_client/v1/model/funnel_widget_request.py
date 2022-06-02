# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FunnelWidgetRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.funnel_query import FunnelQuery
        from datadog_api_client.v1.model.funnel_request_type import FunnelRequestType

        return {
            "query": (FunnelQuery,),
            "request_type": (FunnelRequestType,),
        }

    attribute_map = {
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(self, query, request_type, *args, **kwargs):
        """
        Updated funnel widget.

        :param query: Updated funnel widget.
        :type query: FunnelQuery

        :param request_type: Widget request type.
        :type request_type: FunnelRequestType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.query = query
        self.request_type = request_type

    @classmethod
    def _from_openapi_data(cls, query, request_type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(FunnelWidgetRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.query = query
        self.request_type = request_type
        return self
