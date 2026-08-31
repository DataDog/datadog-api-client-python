# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.usage_quota_response_data import UsageQuotaResponseData
    from datadog_api_client.v2.model.usage_quotas_response_meta import UsageQuotasResponseMeta


class UsageQuotasListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_quota_response_data import UsageQuotaResponseData
        from datadog_api_client.v2.model.usage_quotas_response_meta import UsageQuotasResponseMeta

        return {
            "data": ([UsageQuotaResponseData],),
            "meta": (UsageQuotasResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[UsageQuotaResponseData], meta: UsageQuotasResponseMeta, **kwargs):
        """
        Response containing a paginated list of usage quotas.

        :param data: A list of usage quota resources.
        :type data: [UsageQuotaResponseData]

        :param meta: Pagination metadata for a usage quota list response.
        :type meta: UsageQuotasResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
