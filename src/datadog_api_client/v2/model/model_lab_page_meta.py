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
    from datadog_api_client.v2.model.model_lab_page_meta_page import ModelLabPageMetaPage


class ModelLabPageMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_page_meta_page import ModelLabPageMetaPage

        return {
            "page": (ModelLabPageMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: ModelLabPageMetaPage, **kwargs):
        """
        Pagination metadata for a list response.

        :param page: Pagination details for a list response.
        :type page: ModelLabPageMetaPage
        """
        super().__init__(kwargs)

        self_.page = page
