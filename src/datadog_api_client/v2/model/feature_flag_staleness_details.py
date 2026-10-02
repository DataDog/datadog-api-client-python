# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.feature_flag_staleness_code_reference import FeatureFlagStalenessCodeReference
    from datadog_api_client.v2.model.feature_flag_staleness_recommended_action import (
        FeatureFlagStalenessRecommendedAction,
    )


class FeatureFlagStalenessDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_staleness_code_reference import FeatureFlagStalenessCodeReference
        from datadog_api_client.v2.model.feature_flag_staleness_recommended_action import (
            FeatureFlagStalenessRecommendedAction,
        )

        return {
            "code_references": ([FeatureFlagStalenessCodeReference], none_type),
            "dismissed_by": (str, none_type),
            "id": (str,),
            "recommended_actions": ([FeatureFlagStalenessRecommendedAction], none_type),
            "skip_state_check_until": (datetime, none_type),
            "stale_reason": (str, none_type),
            "staleness_status": (str,),
        }

    attribute_map = {
        "code_references": "code_references",
        "dismissed_by": "dismissed_by",
        "id": "id",
        "recommended_actions": "recommended_actions",
        "skip_state_check_until": "skip_state_check_until",
        "stale_reason": "stale_reason",
        "staleness_status": "staleness_status",
    }

    def __init__(
        self_,
        code_references: Union[List[FeatureFlagStalenessCodeReference], none_type, UnsetType] = unset,
        dismissed_by: Union[str, none_type, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        recommended_actions: Union[List[FeatureFlagStalenessRecommendedAction], none_type, UnsetType] = unset,
        skip_state_check_until: Union[datetime, none_type, UnsetType] = unset,
        stale_reason: Union[str, none_type, UnsetType] = unset,
        staleness_status: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The feature flag's current staleness state and suggested actions.

        :param code_references: Repositories and files where the flag is referenced in source code.
        :type code_references: [FeatureFlagStalenessCodeReference], none_type, optional

        :param dismissed_by: The ID of the user who dismissed the staleness recommendation.
        :type dismissed_by: str, none_type, optional

        :param id: The ID of the feature flag whose staleness state is returned.
        :type id: str, optional

        :param recommended_actions: Suggested actions for the flag. The first action is the primary recommendation.
        :type recommended_actions: [FeatureFlagStalenessRecommendedAction], none_type, optional

        :param skip_state_check_until: Time until which staleness checks are paused for the flag.
        :type skip_state_check_until: datetime, none_type, optional

        :param stale_reason: Why the flag is stale or has a manually selected state. Values include ``FULLY_ROLLED_OUT`` , ``NO_EVALUATIONS`` , ``NO_ACTIVITY`` , and ``USER_SET``.
        :type stale_reason: str, none_type, optional

        :param staleness_status: The current state, such as ``ACTIVE`` , ``STALE`` , or ``PERMANENT``.
        :type staleness_status: str, optional
        """
        if code_references is not unset:
            kwargs["code_references"] = code_references
        if dismissed_by is not unset:
            kwargs["dismissed_by"] = dismissed_by
        if id is not unset:
            kwargs["id"] = id
        if recommended_actions is not unset:
            kwargs["recommended_actions"] = recommended_actions
        if skip_state_check_until is not unset:
            kwargs["skip_state_check_until"] = skip_state_check_until
        if stale_reason is not unset:
            kwargs["stale_reason"] = stale_reason
        if staleness_status is not unset:
            kwargs["staleness_status"] = staleness_status
        super().__init__(kwargs)
