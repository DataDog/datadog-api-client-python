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


class AggregateFilteredQueryFiltersItems(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "base_attribute": (str,),
            "exclude": (bool,),
            "filter_attribute": (str,),
        }

    attribute_map = {
        "base_attribute": "base_attribute",
        "exclude": "exclude",
        "filter_attribute": "filter_attribute",
    }

    def __init__(self_, base_attribute: str, filter_attribute: str, exclude: Union[bool, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param base_attribute: Test-only generated schema for the dashboard versioning proof of concept.
        :type base_attribute: str

        :param exclude: Test-only generated schema for the dashboard versioning proof of concept.
        :type exclude: bool, optional

        :param filter_attribute: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter_attribute: str
        """
        if exclude is not unset:
            kwargs["exclude"] = exclude
        super().__init__(kwargs)

        self_.base_attribute = base_attribute
        self_.filter_attribute = filter_attribute
