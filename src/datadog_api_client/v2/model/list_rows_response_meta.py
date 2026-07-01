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
    from datadog_api_client.v2.model.list_rows_response_meta_page import ListRowsResponseMetaPage


class ListRowsResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_rows_response_meta_page import ListRowsResponseMetaPage

        return {
            "page": (ListRowsResponseMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[ListRowsResponseMetaPage, UnsetType] = unset, **kwargs):
        """
        Contains pagination details, including the continuation token for fetching additional rows.

        :param page: Contains the continuation token for navigating to the next page of rows.
        :type page: ListRowsResponseMetaPage, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
