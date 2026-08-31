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
    from datadog_api_client.v2.model.usage_quota_bulk_result_attributes import UsageQuotaBulkResultAttributes
    from datadog_api_client.v2.model.usage_quota_type import UsageQuotaType


class UsageQuotaBulkResultData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_quota_bulk_result_attributes import UsageQuotaBulkResultAttributes
        from datadog_api_client.v2.model.usage_quota_type import UsageQuotaType

        return {
            "attributes": (UsageQuotaBulkResultAttributes,),
            "id": (str,),
            "type": (UsageQuotaType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: UsageQuotaBulkResultAttributes, id: str, type: UsageQuotaType, **kwargs):
        """
        The result of writing one usage quota in a bulk create-or-update request.

        :param attributes: Attributes of a usage quota bulk write result. On success, all fields except ``error`` are present. On failure, only ``error`` is present and the other fields are omitted.
        :type attributes: UsageQuotaBulkResultAttributes

        :param id: An opaque usage quota identifier. Clients must pass this value back verbatim in update and delete requests and must not infer any structure from it.
        :type id: str

        :param type: The JSON:API resource type for a usage quota.
        :type type: UsageQuotaType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
