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
    from datadog_api_client.v2.model.rum_retention_quota_adaptive_config import RumRetentionQuotaAdaptiveConfig
    from datadog_api_client.v2.model.rum_retention_quota_custom_config import RumRetentionQuotaCustomConfig
    from datadog_api_client.v2.model.rum_retention_quota_mode import RumRetentionQuotaMode


class RumRetentionQuotaConfigUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_quota_adaptive_config import RumRetentionQuotaAdaptiveConfig
        from datadog_api_client.v2.model.rum_retention_quota_custom_config import RumRetentionQuotaCustomConfig
        from datadog_api_client.v2.model.rum_retention_quota_mode import RumRetentionQuotaMode

        return {
            "adaptive": (RumRetentionQuotaAdaptiveConfig,),
            "custom": (RumRetentionQuotaCustomConfig,),
            "mode": (RumRetentionQuotaMode,),
        }

    attribute_map = {
        "adaptive": "adaptive",
        "custom": "custom",
        "mode": "mode",
    }

    def __init__(
        self_,
        mode: RumRetentionQuotaMode,
        adaptive: Union[RumRetentionQuotaAdaptiveConfig, UnsetType] = unset,
        custom: Union[RumRetentionQuotaCustomConfig, UnsetType] = unset,
        **kwargs,
    ):
        """
        The RUM retention quota configuration properties to create or update.

        :param adaptive: The configuration used when ``mode`` is ``adaptive``.
        :type adaptive: RumRetentionQuotaAdaptiveConfig, optional

        :param custom: The configuration used when ``mode`` is ``custom``.
        :type custom: RumRetentionQuotaCustomConfig, optional

        :param mode: The retention quota mode. ``custom`` enforces a fixed session limit, while
            ``adaptive`` dynamically adjusts retention.
        :type mode: RumRetentionQuotaMode
        """
        if adaptive is not unset:
            kwargs["adaptive"] = adaptive
        if custom is not unset:
            kwargs["custom"] = custom
        super().__init__(kwargs)

        self_.mode = mode
