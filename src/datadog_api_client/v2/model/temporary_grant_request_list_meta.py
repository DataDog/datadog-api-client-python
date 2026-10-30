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
    from datadog_api_client.v2.model.temporary_grant_request_page import TemporaryGrantRequestPage


class TemporaryGrantRequestListMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporary_grant_request_page import TemporaryGrantRequestPage

        return {
            "page": (TemporaryGrantRequestPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: TemporaryGrantRequestPage, **kwargs):
        """
        Pagination metadata.

        :param page: UUID cursor pagination. A full final page can return a cursor followed by an empty page.
        :type page: TemporaryGrantRequestPage
        """
        super().__init__(kwargs)

        self_.page = page
