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
    from datadog_api_client.v2.model.rum_retention_quota_config_update_attributes import (
        RUMRetentionQuotaConfigUpdateAttributes,
    )
    from datadog_api_client.v2.model.rum_retention_quota_config_type import RUMRetentionQuotaConfigType


class RUMRetentionQuotaConfigUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_quota_config_update_attributes import (
            RUMRetentionQuotaConfigUpdateAttributes,
        )
        from datadog_api_client.v2.model.rum_retention_quota_config_type import RUMRetentionQuotaConfigType

        return {
            "attributes": (RUMRetentionQuotaConfigUpdateAttributes,),
            "id": (str,),
            "type": (RUMRetentionQuotaConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: RUMRetentionQuotaConfigUpdateAttributes, id: str, type: RUMRetentionQuotaConfigType, **kwargs
    ):
        """
        The RUM retention quota configuration to create or update.

        :param attributes: The RUM retention quota configuration properties to create or update.
        :type attributes: RUMRetentionQuotaConfigUpdateAttributes

        :param id: The identifier of the scope the retention quota configuration applies to.
            Must match ``scope_id`` in the path.
        :type id: str

        :param type: The type of the resource, always ``rum_quota_config``.
        :type type: RUMRetentionQuotaConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
