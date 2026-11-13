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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_bandit_optimal_variant_unavailable_reason import (
        ExperimentsBanditOptimalVariantUnavailableReason,
    )
    from datadog_api_client.v2.model.experiments_bandit_status import ExperimentsBanditStatus


class ExperimentsBanditV2ListDTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_optimal_variant_unavailable_reason import (
            ExperimentsBanditOptimalVariantUnavailableReason,
        )
        from datadog_api_client.v2.model.experiments_bandit_status import ExperimentsBanditStatus

        return {
            "created_at": (datetime,),
            "description": (str,),
            "ended_at": (datetime, none_type),
            "metric_id": (UUID, none_type),
            "name": (str,),
            "optimal_variant_key": (str, none_type),
            "optimal_variant_unavailable_reason": (ExperimentsBanditOptimalVariantUnavailableReason,),
            "started_at": (datetime, none_type),
            "status": (ExperimentsBanditStatus,),
            "subject_type_id": (UUID, none_type),
            "tags": ([str],),
            "teams": ([str],),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "ended_at": "ended_at",
        "metric_id": "metric_id",
        "name": "name",
        "optimal_variant_key": "optimal_variant_key",
        "optimal_variant_unavailable_reason": "optimal_variant_unavailable_reason",
        "started_at": "started_at",
        "status": "status",
        "subject_type_id": "subject_type_id",
        "tags": "tags",
        "teams": "teams",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        description: str,
        ended_at: Union[datetime, none_type],
        metric_id: Union[UUID, none_type],
        name: str,
        optimal_variant_key: Union[str, none_type],
        started_at: Union[datetime, none_type],
        status: ExperimentsBanditStatus,
        subject_type_id: Union[UUID, none_type],
        tags: List[str],
        teams: List[str],
        updated_at: datetime,
        optimal_variant_unavailable_reason: Union[ExperimentsBanditOptimalVariantUnavailableReason, UnsetType] = unset,
        **kwargs,
    ):
        """
        Summary of a bandit. Use Get bandit for its setup, active policy, and latest refresh.

        :param created_at: When the bandit was created.
        :type created_at: datetime

        :param description: The bandit's description.
        :type description: str

        :param ended_at: When the bandit was stopped or reached its scheduled end. Null while it hasn't ended.
        :type ended_at: datetime, none_type

        :param metric_id: The metric the bandit optimizes. Null until set on a draft.
        :type metric_id: UUID, none_type

        :param name: The bandit's name.
        :type name: str

        :param optimal_variant_key: The key of the arm most likely to be best, when one arm leads and the bandit is outside warmup. Null otherwise.
        :type optimal_variant_key: str, none_type

        :param optimal_variant_unavailable_reason: Why no optimal variant is reported. Absent when one is, or when the cause isn't known.
        :type optimal_variant_unavailable_reason: ExperimentsBanditOptimalVariantUnavailableReason, optional

        :param started_at: When the bandit started. Null until it starts.
        :type started_at: datetime, none_type

        :param status: The bandit's status. STOPPED means the bandit was stopped and serves the variant chosen then. COMPLETED means it reached its scheduled end and serves its fallback.
        :type status: ExperimentsBanditStatus

        :param subject_type_id: The subject type the bandit randomizes and measures by. Null until set on a draft.
        :type subject_type_id: UUID, none_type

        :param tags: The bandit's tags, without team tags.
        :type tags: [str]

        :param teams: Handles of the teams that own the bandit.
        :type teams: [str]

        :param updated_at: When the bandit was last changed.
        :type updated_at: datetime
        """
        if optimal_variant_unavailable_reason is not unset:
            kwargs["optimal_variant_unavailable_reason"] = optimal_variant_unavailable_reason
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.description = description
        self_.ended_at = ended_at
        self_.metric_id = metric_id
        self_.name = name
        self_.optimal_variant_key = optimal_variant_key
        self_.started_at = started_at
        self_.status = status
        self_.subject_type_id = subject_type_id
        self_.tags = tags
        self_.teams = teams
        self_.updated_at = updated_at
