# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
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

    def __init__(self_, page: OrgGroupPaginationMetaPage, **kwargs):
        """
        Pagination metadata.

        :param page: Page-based pagination details.
        :type page: OrgGroupPaginationMetaPage
        """
        super().__init__(kwargs)

        self_.page = page
