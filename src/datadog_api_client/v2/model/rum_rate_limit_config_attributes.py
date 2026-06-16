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


class RumRateLimitConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_rate_limit_adaptive_config import RumRateLimitAdaptiveConfig
        from datadog_api_client.v2.model.rum_rate_limit_custom_config import RumRateLimitCustomConfig
        from datadog_api_client.v2.model.rum_rate_limit_mode import RumRateLimitMode

        return {
            "adaptive": (RumRateLimitAdaptiveConfig,),
            "custom": (RumRateLimitCustomConfig,),
            "mode": (RumRateLimitMode,),
            "org_id": (int,),
            "updated_at": (str,),
            "updated_by": (str,),
        }

    attribute_map = {
        "adaptive": "adaptive",
        "custom": "custom",
        "mode": "mode",
        "org_id": "org_id",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        mode: RumRateLimitMode,
        org_id: int,
        adaptive: Union[RumRateLimitAdaptiveConfig, UnsetType] = unset,
        custom: Union[RumRateLimitCustomConfig, UnsetType] = unset,
        updated_at: Union[str, UnsetType] = unset,
        updated_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The RUM rate limit configuration properties.

        :param adaptive: The configuration used when ``mode`` is ``adaptive``.
        :type adaptive: RumRateLimitAdaptiveConfig, optional

        :param custom: The configuration used when ``mode`` is ``custom``.
        :type custom: RumRateLimitCustomConfig, optional

        :param mode: The rate limit mode. ``custom`` enforces a fixed session limit, while
            ``adaptive`` dynamically adjusts retention.
        :type mode: RumRateLimitMode

        :param org_id: The ID of the organization the rate limit configuration belongs to.
        :type org_id: int

        :param updated_at: The date the rate limit configuration was last updated.
        :type updated_at: str, optional

        :param updated_by: The handle of the user who last updated the rate limit configuration.
        :type updated_by: str, optional
        """
        if adaptive is not unset:
            kwargs["adaptive"] = adaptive
        if custom is not unset:
            kwargs["custom"] = custom
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)

        self_.mode = mode
        self_.org_id = org_id
