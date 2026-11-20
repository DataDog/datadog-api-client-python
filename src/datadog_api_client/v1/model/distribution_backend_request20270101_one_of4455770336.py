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


class DistributionBackendRequest20270101OneOf4455770336(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "appsecspan_query": (LogQueryDefinition,),
            "style": (RequestStyle,),
        }

    attribute_map = {
        "appsecspan_query": "appsecspan_query",
        "style": "style",
    }

    def __init__(self_, appsecspan_query: LogQueryDefinition, style: Union[RequestStyle, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param appsecspan_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type appsecspan_query: LogQueryDefinition

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: RequestStyle, optional
        """
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.appsecspan_query = appsecspan_query
