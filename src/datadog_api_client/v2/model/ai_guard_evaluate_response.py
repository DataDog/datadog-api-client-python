# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_guard_action import AIGuardAction
    from datadog_api_client.v2.model.ai_guard_sds_finding import AIGuardSdsFinding


class AIGuardEvaluateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_action import AIGuardAction
        from datadog_api_client.v2.model.ai_guard_sds_finding import AIGuardSdsFinding

        return {
            "action": (AIGuardAction,),
            "global_prob": (float,),
            "is_blocking_enabled": (bool,),
            "reason": (str,),
            "sds_findings": ([AIGuardSdsFinding],),
            "tag_probs": ({str: (float,)},),
            "tags": ([str],),
        }

    attribute_map = {
        "action": "action",
        "global_prob": "global_prob",
        "is_blocking_enabled": "is_blocking_enabled",
        "reason": "reason",
        "sds_findings": "sds_findings",
        "tag_probs": "tag_probs",
        "tags": "tags",
    }

    def __init__(
        self_,
        action: AIGuardAction,
        is_blocking_enabled: bool,
        reason: str,
        tag_probs: Dict[str, float],
        tags: List[str],
        global_prob: Union[float, UnsetType] = unset,
        sds_findings: Union[List[AIGuardSdsFinding], UnsetType] = unset,
        **kwargs,
    ):
        """
        The result of the AI Guard evaluation.

        :param action: The action recommendation from the AI Guard evaluation.
        :type action: AIGuardAction

        :param global_prob: The overall threat probability score across all evaluated tags.
        :type global_prob: float, optional

        :param is_blocking_enabled: Whether blocking mode is enabled for this organization.
        :type is_blocking_enabled: bool

        :param reason: A human-readable explanation of the action recommendation.
        :type reason: str

        :param sds_findings: Sensitive data findings detected in the evaluated conversation.
        :type sds_findings: [AIGuardSdsFinding], optional

        :param tag_probs: Probability scores for each evaluated threat tag.
        :type tag_probs: {str: (float,)}

        :param tags: Security threat tags detected in the evaluated conversation.
        :type tags: [str]
        """
        if global_prob is not unset:
            kwargs["global_prob"] = global_prob
        if sds_findings is not unset:
            kwargs["sds_findings"] = sds_findings
        super().__init__(kwargs)

        self_.action = action
        self_.is_blocking_enabled = is_blocking_enabled
        self_.reason = reason
        self_.tag_probs = tag_probs
        self_.tags = tags
