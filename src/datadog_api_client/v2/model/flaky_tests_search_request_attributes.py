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
    from datadog_api_client.v2.model.flaky_tests_search_filter import FlakyTestsSearchFilter
    from datadog_api_client.v2.model.flaky_tests_search_page_options import FlakyTestsSearchPageOptions
    from datadog_api_client.v2.model.flaky_tests_search_sort import FlakyTestsSearchSort


class FlakyTestsSearchRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.flaky_tests_search_filter import FlakyTestsSearchFilter
        from datadog_api_client.v2.model.flaky_tests_search_page_options import FlakyTestsSearchPageOptions
        from datadog_api_client.v2.model.flaky_tests_search_sort import FlakyTestsSearchSort

        return {
            "filter": (FlakyTestsSearchFilter,),
            "page": (FlakyTestsSearchPageOptions,),
            "sort": (FlakyTestsSearchSort,),
        }

    attribute_map = {
        "filter": "filter",
        "page": "page",
        "sort": "sort",
    }

    def __init__(
        self_,
        filter: Union[FlakyTestsSearchFilter, UnsetType] = unset,
        page: Union[FlakyTestsSearchPageOptions, UnsetType] = unset,
        sort: Union[FlakyTestsSearchSort, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for the flaky tests search request.

        :param filter: Search filter settings.
        :type filter: FlakyTestsSearchFilter, optional

        :param page: Pagination attributes for listing flaky tests.
        :type page: FlakyTestsSearchPageOptions, optional

        :param sort: Parameter for sorting flaky test results. The default sort is by ascending Fully Qualified Name (FQN). The FQN is the concatenation of the test module, suite, and name.
        :type sort: FlakyTestsSearchSort, optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if page is not unset:
            kwargs["page"] = page
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)
