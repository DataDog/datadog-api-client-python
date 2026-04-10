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
    from datadog_api_client.v2.model.list_investigations_response_meta_page import ListInvestigationsResponseMetaPage


class ListInvestigationsResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_investigations_response_meta_page import (
            ListInvestigationsResponseMetaPage,
        )

        return {
            "page": (ListInvestigationsResponseMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: ListInvestigationsResponseMetaPage, **kwargs):
        """
        Metadata for the list investigations response.

        :param page: Pagination metadata.
        :type page: ListInvestigationsResponseMetaPage
        """
        super().__init__(kwargs)

        self_.page = page
