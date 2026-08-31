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
    from datadog_api_client.v2.model.usage_quota_update_attributes import UsageQuotaUpdateAttributes
    from datadog_api_client.v2.model.usage_quota_type import UsageQuotaType


class UsageQuotaUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_quota_update_attributes import UsageQuotaUpdateAttributes
        from datadog_api_client.v2.model.usage_quota_type import UsageQuotaType

        return {
            "attributes": (UsageQuotaUpdateAttributes,),
            "id": (str,),
            "type": (UsageQuotaType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: UsageQuotaUpdateAttributes, id: str, type: UsageQuotaType, **kwargs):
        """
        A usage quota resource to update.

        :param attributes: Attributes to update on a usage quota. Omitting a property leaves its current value unchanged.
        :type attributes: UsageQuotaUpdateAttributes

        :param id: The opaque usage quota identifier, which must match the identifier in the request path.
        :type id: str

        :param type: The JSON:API resource type for a usage quota.
        :type type: UsageQuotaType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
