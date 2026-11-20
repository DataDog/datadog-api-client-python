# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SunburstBackendRequest20270101OneOf4462423840(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "ddsql_query": (str,),
            "request_type": (SunburstBackendRequestAnyOfAnyOfItemRequestType4452229632,),
            "response_format": (SunburstBackendRequestAnyOfAnyOfItemResponseFormat4452229952,),
            "style": (SunburstRequestStyle,),
        }

    attribute_map = {
        "ddsql_query": "ddsql_query",
        "request_type": "request_type",
        "response_format": "response_format",
        "style": "style",
    }

    def __init__(
        self_,
        ddsql_query: str,
        request_type: SunburstBackendRequestAnyOfAnyOfItemRequestType4452229632,
        response_format: SunburstBackendRequestAnyOfAnyOfItemResponseFormat4452229952,
        style: Union[SunburstRequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: SunburstBackendRequestAnyOfAnyOfItemRequestType4452229632

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: SunburstBackendRequestAnyOfAnyOfItemResponseFormat4452229952

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: SunburstRequestStyle, optional
        """
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.ddsql_query = ddsql_query
        self_.request_type = request_type
        self_.response_format = response_format
