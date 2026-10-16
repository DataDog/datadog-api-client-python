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
    from datadog_api_client.v2.model.usage_quota_create_attributes import UsageQuotaCreateAttributes
    from datadog_api_client.v2.model.usage_quota_type import UsageQuotaType


class UsageQuotaCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_quota_create_attributes import UsageQuotaCreateAttributes
        from datadog_api_client.v2.model.usage_quota_type import UsageQuotaType

        return {
            "attributes": (UsageQuotaCreateAttributes,),
            "type": (UsageQuotaType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: UsageQuotaCreateAttributes, type: UsageQuotaType, **kwargs):
        """
        A usage quota resource to create or update by scope.

        :param attributes: Attributes for creating or updating a usage quota by scope. Each item must provide ``usage_limit`` , ``pending_usage_limit`` , or both. Providing only ``pending_usage_limit`` updates an existing organization-wide quota, never creates one, requires ``enforced`` to be omitted, and fails if the quota does not exist.
        :type attributes: UsageQuotaCreateAttributes

        :param type: The JSON:API resource type for a usage quota.
        :type type: UsageQuotaType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
