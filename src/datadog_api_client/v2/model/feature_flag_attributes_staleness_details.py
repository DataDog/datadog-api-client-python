# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

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


class FeatureFlagAttributesStalenessDetails(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "code_references": (
                [
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
                    }
                ],
                none_type,
            ),
            "dismissed_by": (UUID, none_type),
            "id": (UUID,),
            "recommended_actions": (
                [
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
                    }
                ],
                none_type,
            ),
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
        code_references: Union[List[Dict[str, Any]], none_type, UnsetType] = unset,
        dismissed_by: Union[UUID, none_type, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        recommended_actions: Union[List[Dict[str, Any]], none_type, UnsetType] = unset,
        skip_state_check_until: Union[datetime, none_type, UnsetType] = unset,
        stale_reason: Union[str, none_type, UnsetType] = unset,
        staleness_status: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details about the feature flag's staleness status.

        :param code_references: Code references associated with the feature flag.
        :type code_references: [{str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}], none_type, optional

        :param dismissed_by: The ID of the user who dismissed the staleness notification.
        :type dismissed_by: UUID, none_type, optional

        :param id: The unique identifier of the staleness details record.
        :type id: UUID, optional

        :param recommended_actions: Recommended actions to address the feature flag's staleness.
        :type recommended_actions: [{str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}], none_type, optional

        :param skip_state_check_until: The timestamp until which staleness checks are skipped.
        :type skip_state_check_until: datetime, none_type, optional

        :param stale_reason: The reason the feature flag is considered stale.
        :type stale_reason: str, none_type, optional

        :param staleness_status: The staleness status of the feature flag.
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
