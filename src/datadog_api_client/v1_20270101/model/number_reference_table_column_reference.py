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


class NumberReferenceTableColumnReference(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "column": (str,),
            "filter": (str,),
            "query": (str,),
        }

    attribute_map = {
        "column": "column",
        "filter": "filter",
        "query": "query",
    }

    def __init__(self_, column: str, query: str, filter: Union[str, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: str
        """
        if filter is not unset:
            kwargs["filter"] = filter
        super().__init__(kwargs)

        self_.column = column
        self_.query = query
