# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_retention_quota_custom_config import RumRetentionQuotaCustomConfig
    from datadog_api_client.v2.model.rum_retention_quota_mode import RumRetentionQuotaMode


class RumRetentionQuotaConfigUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_quota_custom_config import RumRetentionQuotaCustomConfig
        from datadog_api_client.v2.model.rum_retention_quota_mode import RumRetentionQuotaMode

        return {
            "custom": (RumRetentionQuotaCustomConfig,),
            "mode": (RumRetentionQuotaMode,),
        }

    attribute_map = {
        "custom": "custom",
        "mode": "mode",
    }

    def __init__(
        self_, mode: RumRetentionQuotaMode, custom: Union[RumRetentionQuotaCustomConfig, UnsetType] = unset, **kwargs
    ):
        """
        The RUM retention quota configuration properties to create or update.

        :param custom: The configuration used when ``mode`` is ``custom``.
        :type custom: RumRetentionQuotaCustomConfig, optional

        :param mode: The retention quota mode. ``custom`` enforces a fixed session limit.
            ``custom`` is the only supported mode.
        :type mode: RumRetentionQuotaMode
        """
        if custom is not unset:
            kwargs["custom"] = custom
        super().__init__(kwargs)

        self_.mode = mode
