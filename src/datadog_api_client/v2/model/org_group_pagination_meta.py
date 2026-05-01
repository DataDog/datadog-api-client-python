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
    from datadog_api_client.v2.model.org_group_pagination_meta_page import OrgGroupPaginationMetaPage


class OrgGroupPaginationMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_pagination_meta_page import OrgGroupPaginationMetaPage

        return {
            "page": (OrgGroupPaginationMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[OrgGroupPaginationMetaPage, UnsetType] = unset, **kwargs):
        """
        Pagination metadata for org group list responses.

        :param page: Page-based pagination details for org group list responses.
        :type page: OrgGroupPaginationMetaPage, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
