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
    from datadog_api_client.v2.model.usage_quota_create_data import UsageQuotaCreateData


class UsageQuotasCreateRequest(ModelNormal):
    validations = {
        "data": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_quota_create_data import UsageQuotaCreateData

        return {
            "data": ([UsageQuotaCreateData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[UsageQuotaCreateData], **kwargs):
        """
        A JSON:API bulk request containing an array of usage quota resources rather than a single resource.

        :param data: A bulk list of usage quota resources to create or update by scope.
        :type data: [UsageQuotaCreateData]
        """
        super().__init__(kwargs)

        self_.data = data
