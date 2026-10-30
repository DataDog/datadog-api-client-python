# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_guard_confidence_threshold_override import AIGuardConfidenceThresholdOverride
    from datadog_api_client.v2.model.ai_guard_tool_policy_action import AIGuardToolPolicyAction
    from datadog_api_client.v2.model.ai_guard_confidence_threshold import AIGuardConfidenceThreshold


class AIGuardMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_confidence_threshold_override import (
            AIGuardConfidenceThresholdOverride,
        )
        from datadog_api_client.v2.model.ai_guard_tool_policy_action import AIGuardToolPolicyAction

        return {
            "coding_agent": (str,),
            "confidence_threshold": (AIGuardConfidenceThresholdOverride,),
            "env": (str,),
            "is_sds_enabled_override": (bool,),
            "service": (str,),
            "tool_policies": ({str: (AIGuardToolPolicyAction,)},),
        }

    attribute_map = {
        "coding_agent": "coding_agent",
        "confidence_threshold": "confidence_threshold",
        "env": "env",
        "is_sds_enabled_override": "is_sds_enabled_override",
        "service": "service",
        "tool_policies": "tool_policies",
    }

    def __init__(
        self_,
        coding_agent: Union[str, UnsetType] = unset,
        confidence_threshold: Union[
            AIGuardConfidenceThresholdOverride, float, AIGuardConfidenceThreshold, UnsetType
        ] = unset,
        env: Union[str, UnsetType] = unset,
        is_sds_enabled_override: Union[bool, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        tool_policies: Union[Dict[str, AIGuardToolPolicyAction], UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the evaluated conversation, used to select the policy and evaluator behavior.

        :param coding_agent: The coding agent that produced the conversation. By default, a non-empty
            value selects the coding-agent evaluator profile, while an omitted or empty
            value selects the default profile. Known identifiers include ``claude-code`` ,
            ``codex`` , ``cursor`` , and ``github-copilot`` ; other identifiers are accepted.
            The coding-agent profile assumes the caller can ask the user to confirm
            Supply Chain Firewall warnings; the default profile assumes it cannot.
        :type coding_agent: str, optional

        :param confidence_threshold: Request-only confidence threshold override. A number sets the threshold
            for every threat category; an object supplies a global threshold and
            optional per-category overrides. Omit this field to use the stored
            sensitivity policy. This field is not returned in evaluation responses.
        :type confidence_threshold: AIGuardConfidenceThresholdOverride, optional

        :param env: The environment the conversation belongs to.
        :type env: str, optional

        :param is_sds_enabled_override: Whether to run the Sensitive Data Scanner for this request, overriding the stored policy.
        :type is_sds_enabled_override: bool, optional

        :param service: The name of the service the conversation belongs to.
        :type service: str, optional

        :param tool_policies: A non-empty map replaces stored tool policies for this request only,
            keyed by tool name. Any called tool not present resolves to EVALUATE.
            Only takes effect when tool policies are enabled for the organization.
        :type tool_policies: {str: (AIGuardToolPolicyAction,)}, optional
        """
        if coding_agent is not unset:
            kwargs["coding_agent"] = coding_agent
        if confidence_threshold is not unset:
            kwargs["confidence_threshold"] = confidence_threshold
        if env is not unset:
            kwargs["env"] = env
        if is_sds_enabled_override is not unset:
            kwargs["is_sds_enabled_override"] = is_sds_enabled_override
        if service is not unset:
            kwargs["service"] = service
        if tool_policies is not unset:
            kwargs["tool_policies"] = tool_policies
        super().__init__(kwargs)
