# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.feature_flag_targeting_rule import FeatureFlagTargetingRule
    from datadog_api_client.v2.model.feature_flag_status import FeatureFlagStatus


class FeatureFlagEnvironment(ModelNormal):
    validations = {
        "rollout_percentage": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_targeting_rule import FeatureFlagTargetingRule
        from datadog_api_client.v2.model.feature_flag_status import FeatureFlagStatus

        return {
            "allocations": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
                none_type,
            ),
            "default_allocation_key": (str,),
            "default_variant_id": (str, none_type),
            "environment_id": (UUID,),
            "environment_name": (str,),
            "environment_queries": ([str],),
            "is_production": (bool,),
            "override_allocation_key": (str,),
            "override_variant_id": (str, none_type),
            "pending_suggestion_id": (str, none_type),
            "require_feature_flag_approval": (bool,),
            "rollout_percentage": (int,),
            "rules": ([FeatureFlagTargetingRule],),
            "status": (FeatureFlagStatus,),
        }

    attribute_map = {
        "allocations": "allocations",
        "default_allocation_key": "default_allocation_key",
        "default_variant_id": "default_variant_id",
        "environment_id": "environment_id",
        "environment_name": "environment_name",
        "environment_queries": "environment_queries",
        "is_production": "is_production",
        "override_allocation_key": "override_allocation_key",
        "override_variant_id": "override_variant_id",
        "pending_suggestion_id": "pending_suggestion_id",
        "require_feature_flag_approval": "require_feature_flag_approval",
        "rollout_percentage": "rollout_percentage",
        "rules": "rules",
        "status": "status",
    }

    def __init__(
        self_,
        environment_id: UUID,
        status: FeatureFlagStatus,
        allocations: Union[Dict[str, Any], none_type, UnsetType] = unset,
        default_allocation_key: Union[str, UnsetType] = unset,
        default_variant_id: Union[str, none_type, UnsetType] = unset,
        environment_name: Union[str, UnsetType] = unset,
        environment_queries: Union[List[str], UnsetType] = unset,
        is_production: Union[bool, UnsetType] = unset,
        override_allocation_key: Union[str, UnsetType] = unset,
        override_variant_id: Union[str, none_type, UnsetType] = unset,
        pending_suggestion_id: Union[str, none_type, UnsetType] = unset,
        require_feature_flag_approval: Union[bool, UnsetType] = unset,
        rollout_percentage: Union[int, UnsetType] = unset,
        rules: Union[List[FeatureFlagTargetingRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        Environment-specific settings for a feature flag.

        :param allocations: Allocation metadata for this environment.
        :type allocations: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param default_allocation_key: The allocation key used for the default variant.
        :type default_allocation_key: str, optional

        :param default_variant_id: The ID of the default variant for this environment.
        :type default_variant_id: str, none_type, optional

        :param environment_id: The ID of the environment.
        :type environment_id: UUID

        :param environment_name: The name of the environment.
        :type environment_name: str, optional

        :param environment_queries: Queries that target this environment.
        :type environment_queries: [str], optional

        :param is_production: Indicates whether the environment is production.
        :type is_production: bool, optional

        :param override_allocation_key: The allocation key used for the override variant.
        :type override_allocation_key: str, optional

        :param override_variant_id: The ID of the override variant for this environment.
        :type override_variant_id: str, none_type, optional

        :param pending_suggestion_id: Pending suggestion identifier, if approval is required.
        :type pending_suggestion_id: str, none_type, optional

        :param require_feature_flag_approval: Indicates whether feature flag changes require approval in this environment.
        :type require_feature_flag_approval: bool, optional

        :param rollout_percentage: Rollout percentage for this environment.
        :type rollout_percentage: int, optional

        :param rules: Environment targeting rules for this feature flag.
        :type rules: [FeatureFlagTargetingRule], optional

        :param status: The status of a feature flag in an environment.
        :type status: FeatureFlagStatus
        """
        if allocations is not unset:
            kwargs["allocations"] = allocations
        if default_allocation_key is not unset:
            kwargs["default_allocation_key"] = default_allocation_key
        if default_variant_id is not unset:
            kwargs["default_variant_id"] = default_variant_id
        if environment_name is not unset:
            kwargs["environment_name"] = environment_name
        if environment_queries is not unset:
            kwargs["environment_queries"] = environment_queries
        if is_production is not unset:
            kwargs["is_production"] = is_production
        if override_allocation_key is not unset:
            kwargs["override_allocation_key"] = override_allocation_key
        if override_variant_id is not unset:
            kwargs["override_variant_id"] = override_variant_id
        if pending_suggestion_id is not unset:
            kwargs["pending_suggestion_id"] = pending_suggestion_id
        if require_feature_flag_approval is not unset:
            kwargs["require_feature_flag_approval"] = require_feature_flag_approval
        if rollout_percentage is not unset:
            kwargs["rollout_percentage"] = rollout_percentage
        if rules is not unset:
            kwargs["rules"] = rules
        super().__init__(kwargs)

        self_.environment_id = environment_id
        self_.status = status
