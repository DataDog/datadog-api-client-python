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
    from datadog_api_client.v1.model.retention_query import RetentionQuery
    from datadog_api_client.v1.model.retention_curve_request_type import RetentionCurveRequestType
    from datadog_api_client.v1.model.retention_curve_style import RetentionCurveStyle


class RetentionCurveWidgetRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.retention_query import RetentionQuery
        from datadog_api_client.v1.model.retention_curve_request_type import RetentionCurveRequestType
        from datadog_api_client.v1.model.retention_curve_style import RetentionCurveStyle

        return {
            "query": (RetentionQuery,),
            "request_type": (RetentionCurveRequestType,),
            "style": (RetentionCurveStyle,),
        }

    attribute_map = {
        "query": "query",
        "request_type": "request_type",
        "style": "style",
    }

    def __init__(
        self_,
        query: RetentionQuery,
        request_type: RetentionCurveRequestType,
        style: Union[RetentionCurveStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Retention curve widget request.

        :param query: Retention query definition.
        :type query: RetentionQuery

        :param request_type: Request type for retention curve widget.
        :type request_type: RetentionCurveRequestType

        :param style: Style configuration for retention curve.
        :type style: RetentionCurveStyle, optional
        """
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
