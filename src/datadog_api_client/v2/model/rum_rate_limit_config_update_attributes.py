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
    from datadog_api_client.v2.model.rum_rate_limit_adaptive_config import RumRateLimitAdaptiveConfig
    from datadog_api_client.v2.model.rum_rate_limit_custom_config import RumRateLimitCustomConfig
    from datadog_api_client.v2.model.rum_rate_limit_mode import RumRateLimitMode


class RumRateLimitConfigUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_rate_limit_adaptive_config import RumRateLimitAdaptiveConfig
        from datadog_api_client.v2.model.rum_rate_limit_custom_config import RumRateLimitCustomConfig
        from datadog_api_client.v2.model.rum_rate_limit_mode import RumRateLimitMode

        return {
            "adaptive": (RumRateLimitAdaptiveConfig,),
            "custom": (RumRateLimitCustomConfig,),
            "mode": (RumRateLimitMode,),
        }

    attribute_map = {
        "adaptive": "adaptive",
        "custom": "custom",
        "mode": "mode",
    }

    def __init__(
        self_,
        mode: RumRateLimitMode,
        adaptive: Union[RumRateLimitAdaptiveConfig, UnsetType] = unset,
        custom: Union[RumRateLimitCustomConfig, UnsetType] = unset,
        **kwargs,
    ):
        """
        The RUM rate limit configuration properties to create or update.

        :param adaptive: The configuration used when ``mode`` is ``adaptive``.
        :type adaptive: RumRateLimitAdaptiveConfig, optional

        :param custom: The configuration used when ``mode`` is ``custom``.
        :type custom: RumRateLimitCustomConfig, optional

        :param mode: The rate limit mode. ``custom`` enforces a fixed session limit, while
            ``adaptive`` dynamically adjusts retention.
        :type mode: RumRateLimitMode
        """
        if adaptive is not unset:
            kwargs["adaptive"] = adaptive
        if custom is not unset:
            kwargs["custom"] = custom
        super().__init__(kwargs)

        self_.mode = mode
