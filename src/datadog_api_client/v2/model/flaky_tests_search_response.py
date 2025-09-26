# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.flaky_test import FlakyTest
    from datadog_api_client.v2.model.flaky_tests_search_response_meta import FlakyTestsSearchResponseMeta


class FlakyTestsSearchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.flaky_test import FlakyTest
        from datadog_api_client.v2.model.flaky_tests_search_response_meta import FlakyTestsSearchResponseMeta

        return {
            "data": ([FlakyTest],),
            "meta": (FlakyTestsSearchResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[FlakyTest], UnsetType] = unset,
        meta: Union[FlakyTestsSearchResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object with flaky tests matching the search request.

        :param data: Array of flaky tests matching the request.
        :type data: [FlakyTest], optional

        :param meta: Metadata for the flaky tests search response.
        :type meta: FlakyTestsSearchResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
