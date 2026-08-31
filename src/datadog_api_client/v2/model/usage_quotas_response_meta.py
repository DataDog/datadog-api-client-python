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
    from datadog_api_client.v2.model.usage_quotas_response_meta_page import UsageQuotasResponseMetaPage


class UsageQuotasResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_quotas_response_meta_page import UsageQuotasResponseMetaPage

        return {
            "page": (UsageQuotasResponseMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: UsageQuotasResponseMetaPage, **kwargs):
        """
        Pagination metadata for a usage quota list response.

        :param page: Cursor pagination fields for a usage quota list response.
        :type page: UsageQuotasResponseMetaPage
        """
        super().__init__(kwargs)

        self_.page = page
