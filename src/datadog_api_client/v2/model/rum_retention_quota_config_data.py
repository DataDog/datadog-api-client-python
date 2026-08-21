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
    from datadog_api_client.v2.model.rum_retention_quota_config_attributes import RumRetentionQuotaConfigAttributes
    from datadog_api_client.v2.model.rum_retention_quota_config_type import RumRetentionQuotaConfigType


class RumRetentionQuotaConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_quota_config_attributes import RumRetentionQuotaConfigAttributes
        from datadog_api_client.v2.model.rum_retention_quota_config_type import RumRetentionQuotaConfigType

        return {
            "attributes": (RumRetentionQuotaConfigAttributes,),
            "id": (str,),
            "type": (RumRetentionQuotaConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: RumRetentionQuotaConfigAttributes, id: str, type: RumRetentionQuotaConfigType, **kwargs
    ):
        """
        The RUM retention quota configuration object.

        :param attributes: The RUM retention quota configuration properties.
        :type attributes: RumRetentionQuotaConfigAttributes

        :param id: The identifier of the scope the retention quota configuration applies to.
        :type id: str

        :param type: The type of the resource, always ``rum_quota_config``.
        :type type: RumRetentionQuotaConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
