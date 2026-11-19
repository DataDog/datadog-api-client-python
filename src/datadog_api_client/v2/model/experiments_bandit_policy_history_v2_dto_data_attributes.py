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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_bandit_policy_kind import ExperimentsBanditPolicyKind
    from datadog_api_client.v2.model.experiments_bandit_policy_reason import ExperimentsBanditPolicyReason
    from datadog_api_client.v2.model.experiments_bandit_policy_variant_v2 import ExperimentsBanditPolicyVariantV2


class ExperimentsBanditPolicyHistoryV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_policy_kind import ExperimentsBanditPolicyKind
        from datadog_api_client.v2.model.experiments_bandit_policy_reason import ExperimentsBanditPolicyReason
        from datadog_api_client.v2.model.experiments_bandit_policy_variant_v2 import ExperimentsBanditPolicyVariantV2

        return {
            "applied_at": (datetime,),
            "config_version": (int,),
            "is_active": (bool,),
            "kind": (ExperimentsBanditPolicyKind,),
            "policy_number": (int,),
            "reason": (ExperimentsBanditPolicyReason,),
            "refresh_id": (UUID, none_type),
            "variants": ([ExperimentsBanditPolicyVariantV2],),
        }

    attribute_map = {
        "applied_at": "applied_at",
        "config_version": "config_version",
        "is_active": "is_active",
        "kind": "kind",
        "policy_number": "policy_number",
        "reason": "reason",
        "refresh_id": "refresh_id",
        "variants": "variants",
    }

    def __init__(
        self_,
        applied_at: datetime,
        config_version: int,
        is_active: bool,
        kind: ExperimentsBanditPolicyKind,
        policy_number: int,
        reason: ExperimentsBanditPolicyReason,
        refresh_id: Union[UUID, none_type],
        variants: List[ExperimentsBanditPolicyVariantV2],
        **kwargs,
    ):
        """
        A traffic split the bandit served, with the same fields as ``active_policy``.

        :param applied_at: When the policy was saved. SDKs pick it up on their next configuration fetch.
        :type applied_at: datetime

        :param config_version: The configuration version the policy was made for.
        :type config_version: int

        :param is_active: Whether this is the policy the bandit serves now, the one Get bandit returns as ``active_policy``. A paused bandit keeps serving it, and an ended bandit serves its fallback.
        :type is_active: bool

        :param kind: ``WARMUP`` serves the arms equally. ``ADAPTIVE`` serves the initial split or a split from a refresh. ``FALLBACK`` serves one variant after the bandit ends.
        :type kind: ExperimentsBanditPolicyKind

        :param policy_number: The policy's place in the bandit's policy history. It follows ``applied_at`` and orders policies saved at the same time.
        :type policy_number: int

        :param reason: Why the policy was applied.
        :type reason: ExperimentsBanditPolicyReason

        :param refresh_id: The refresh that proposed the policy. ``null`` for policies no refresh proposed, such as the first split and the policy served after the bandit ends.
        :type refresh_id: UUID, none_type

        :param variants: Each variant's share of traffic. The probabilities add up to 1. A variant served as an arm keeps the key the arm had, even if the arm was removed later.
        :type variants: [ExperimentsBanditPolicyVariantV2]
        """
        super().__init__(kwargs)

        self_.applied_at = applied_at
        self_.config_version = config_version
        self_.is_active = is_active
        self_.kind = kind
        self_.policy_number = policy_number
        self_.reason = reason
        self_.refresh_id = refresh_id
        self_.variants = variants
