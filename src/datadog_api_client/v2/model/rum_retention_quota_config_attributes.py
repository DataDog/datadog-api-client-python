# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_retention_quota_custom_config import RumRetentionQuotaCustomConfig
    from datadog_api_client.v2.model.rum_retention_quota_mode import RumRetentionQuotaMode


class RumRetentionQuotaConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_quota_custom_config import RumRetentionQuotaCustomConfig
        from datadog_api_client.v2.model.rum_retention_quota_mode import RumRetentionQuotaMode

        return {
            "custom": (RumRetentionQuotaCustomConfig,),
            "mode": (RumRetentionQuotaMode,),
            "org_id": (int,),
            "updated_at": (datetime,),
            "updated_by": (str,),
        }

    attribute_map = {
        "custom": "custom",
        "mode": "mode",
        "org_id": "org_id",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        mode: RumRetentionQuotaMode,
        org_id: int,
        custom: Union[RumRetentionQuotaCustomConfig, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        updated_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The RUM retention quota configuration properties.

        :param custom: The configuration used when ``mode`` is ``custom``.
        :type custom: RumRetentionQuotaCustomConfig, optional

        :param mode: The retention quota mode. ``custom`` enforces a fixed session limit.
            ``custom`` is the only supported mode.
        :type mode: RumRetentionQuotaMode

        :param org_id: The ID of the organization the retention quota configuration belongs to.
        :type org_id: int

        :param updated_at: The date the retention quota configuration was last updated.
        :type updated_at: datetime, optional

        :param updated_by: The handle of the user who last updated the retention quota configuration.
        :type updated_by: str, optional
        """
        if custom is not unset:
            kwargs["custom"] = custom
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)

        self_.mode = mode
        self_.org_id = org_id
