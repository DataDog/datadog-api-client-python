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
    from datadog_api_client.v2.model.model_lab_run_data import ModelLabRunData
    from datadog_api_client.v2.model.model_lab_pagination_links import ModelLabPaginationLinks
    from datadog_api_client.v2.model.model_lab_page_meta import ModelLabPageMeta


class ModelLabRunsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_run_data import ModelLabRunData
        from datadog_api_client.v2.model.model_lab_pagination_links import ModelLabPaginationLinks
        from datadog_api_client.v2.model.model_lab_page_meta import ModelLabPageMeta

        return {
            "data": ([ModelLabRunData],),
            "links": (ModelLabPaginationLinks,),
            "meta": (ModelLabPageMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[ModelLabRunData],
        meta: ModelLabPageMeta,
        links: Union[ModelLabPaginationLinks, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a list of Model Lab runs with pagination metadata.

        :param data: The list of runs.
        :type data: [ModelLabRunData]

        :param links: Pagination links for navigating list responses.
        :type links: ModelLabPaginationLinks, optional

        :param meta: Pagination metadata for a list response.
        :type meta: ModelLabPageMeta
        """
        if links is not unset:
            kwargs["links"] = links
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
