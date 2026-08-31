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
    from datadog_api_client.v2.model.usage_quota_bulk_result_data import UsageQuotaBulkResultData


class UsageQuotasBulkResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_quota_bulk_result_data import UsageQuotaBulkResultData

        return {
            "data": ([UsageQuotaBulkResultData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[UsageQuotaBulkResultData], **kwargs):
        """
        Response containing the result of a bulk usage quota create-or-update request. Returned with a ``200`` status regardless of whether individual items succeeded or failed; check each item's ``error`` attribute to determine its outcome.

        :param data: The results of writing each usage quota in a bulk create-or-update request, in the same order as the request.
        :type data: [UsageQuotaBulkResultData]
        """
        super().__init__(kwargs)

        self_.data = data
