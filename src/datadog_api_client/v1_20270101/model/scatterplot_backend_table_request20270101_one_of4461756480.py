# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.scatterplot_projection import ScatterplotProjection
    from datadog_api_client.v1_20270101.model.events_platform_data_projection_query import (
        EventsPlatformDataProjectionQuery,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request_any_of_any_of_item_request_type4451375104 import (
        ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451375104,
    )


class ScatterplotBackendTableRequest20270101OneOf4461756480(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scatterplot_projection import ScatterplotProjection
        from datadog_api_client.v1_20270101.model.events_platform_data_projection_query import (
            EventsPlatformDataProjectionQuery,
        )
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request_any_of_any_of_item_request_type4451375104 import (
            ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451375104,
        )

        return {
            "limit": (float,),
            "projection": (ScatterplotProjection,),
            "query": (EventsPlatformDataProjectionQuery,),
            "request_type": (ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451375104,),
        }

    attribute_map = {
        "limit": "limit",
        "projection": "projection",
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(
        self_,
        projection: ScatterplotProjection,
        query: EventsPlatformDataProjectionQuery,
        request_type: ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451375104,
        limit: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: ScatterplotProjection

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: EventsPlatformDataProjectionQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451375104
        """
        if limit is not unset:
            kwargs["limit"] = limit
        super().__init__(kwargs)

        self_.projection = projection
        self_.query = query
        self_.request_type = request_type
