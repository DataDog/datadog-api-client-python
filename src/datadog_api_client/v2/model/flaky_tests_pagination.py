# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class FlakyTestsPagination(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next_page": (str, none_type),
        }

    attribute_map = {
        "next_page": "next_page",
    }

    def __init__(self_, next_page: Union[str, none_type, UnsetType] = unset, **kwargs):
        """
        Pagination metadata for flaky tests.

        :param next_page: Cursor for the next page of results.
        :type next_page: str, none_type, optional
        """
        if next_page is not unset:
            kwargs["next_page"] = next_page
        super().__init__(kwargs)
