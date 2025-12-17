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
    from datadog_api_client.v2.model.security_findings_search_request_page import SecurityFindingsSearchRequestPage
    from datadog_api_client.v2.model.security_findings_sort import SecurityFindingsSort


class SecurityFindingsSearchRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_findings_search_request_page import SecurityFindingsSearchRequestPage
        from datadog_api_client.v2.model.security_findings_sort import SecurityFindingsSort

        return {
            "filter": (str,),
            "page": (SecurityFindingsSearchRequestPage,),
            "sort": (SecurityFindingsSort,),
        }

    attribute_map = {
        "filter": "filter",
        "page": "page",
        "sort": "sort",
    }

    def __init__(
        self_,
        filter: Union[str, UnsetType] = unset,
        page: Union[SecurityFindingsSearchRequestPage, UnsetType] = unset,
        sort: Union[SecurityFindingsSort, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request attributes for searching security findings.

        :param filter: The search query following log search syntax.
        :type filter: str, optional

        :param page: Pagination attributes for the search request.
        :type page: SecurityFindingsSearchRequestPage, optional

        :param sort: The sort parameters when querying security findings.
        :type sort: SecurityFindingsSort, optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if page is not unset:
            kwargs["page"] = page
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)
