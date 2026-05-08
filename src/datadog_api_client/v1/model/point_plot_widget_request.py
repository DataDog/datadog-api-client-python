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
    from datadog_api_client.v1.model.point_plot_projection import PointPlotProjection
    from datadog_api_client.v1.model.data_projection_query import DataProjectionQuery
    from datadog_api_client.v1.model.data_projection_request_type import DataProjectionRequestType


class PointPlotWidgetRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.point_plot_projection import PointPlotProjection
        from datadog_api_client.v1.model.data_projection_query import DataProjectionQuery
        from datadog_api_client.v1.model.data_projection_request_type import DataProjectionRequestType

        return {
            "limit": (int,),
            "projection": (PointPlotProjection,),
            "query": (DataProjectionQuery,),
            "request_type": (DataProjectionRequestType,),
        }

    attribute_map = {
        "limit": "limit",
        "projection": "projection",
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(
        self_,
        projection: PointPlotProjection,
        query: DataProjectionQuery,
        request_type: DataProjectionRequestType,
        limit: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request configuration for the point plot widget.

        :param limit: Maximum number of data points to return.
        :type limit: int, optional

        :param projection: Projection configuration for the point plot widget.
        :type projection: PointPlotProjection

        :param query: Query configuration for a data projection request.
        :type query: DataProjectionQuery

        :param request_type: Type of a data projection request.
        :type request_type: DataProjectionRequestType
        """
        if limit is not unset:
            kwargs["limit"] = limit
        super().__init__(kwargs)

        self_.projection = projection
        self_.query = query
        self_.request_type = request_type
