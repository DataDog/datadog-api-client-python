# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_guard_action import AIGuardAction
    from datadog_api_client.v2.model.ai_guard_redaction_replacement import AIGuardRedactionReplacement
    from datadog_api_client.v2.model.ai_guard_scfw_findings import AIGuardScfwFindings
    from datadog_api_client.v2.model.ai_guard_sds_finding import AIGuardSdsFinding


class AIGuardEvaluateAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_action import AIGuardAction
        from datadog_api_client.v2.model.ai_guard_redaction_replacement import AIGuardRedactionReplacement
        from datadog_api_client.v2.model.ai_guard_scfw_findings import AIGuardScfwFindings
        from datadog_api_client.v2.model.ai_guard_sds_finding import AIGuardSdsFinding

        return {
            "action": (AIGuardAction,),
            "global_prob": (float,),
            "is_blocking_enabled": (bool,),
            "reason": (str,),
            "redaction_replacements": ([AIGuardRedactionReplacement],),
            "scfw_findings": (AIGuardScfwFindings,),
            "sds_findings": ([AIGuardSdsFinding],),
            "tag_probs": ({str: (float,)}, none_type),
            "tags": ([str],),
        }

    attribute_map = {
        "action": "action",
        "global_prob": "global_prob",
        "is_blocking_enabled": "is_blocking_enabled",
        "reason": "reason",
        "redaction_replacements": "redaction_replacements",
        "scfw_findings": "scfw_findings",
        "sds_findings": "sds_findings",
        "tag_probs": "tag_probs",
        "tags": "tags",
    }

    def __init__(
        self_,
        action: AIGuardAction,
        is_blocking_enabled: bool,
        reason: str,
        tag_probs: Union[Dict[str, float], none_type],
        tags: List[str],
        global_prob: Union[float, UnsetType] = unset,
        redaction_replacements: Union[List[AIGuardRedactionReplacement], UnsetType] = unset,
        scfw_findings: Union[AIGuardScfwFindings, UnsetType] = unset,
        sds_findings: Union[List[AIGuardSdsFinding], UnsetType] = unset,
        **kwargs,
    ):
        """
        The evaluation result with the recommended action and detected threat information.

        :param action: The recommended action for the evaluated conversation.
        :type action: AIGuardAction

        :param global_prob: The global threat probability, between ``0`` and ``1``. Included only when computed.
        :type global_prob: float, optional

        :param is_blocking_enabled: Whether blocking is enabled for the organization.
        :type is_blocking_enabled: bool

        :param reason: The explanation for the recommended action, for logging rather than user-facing display.
        :type reason: str

        :param redaction_replacements: The redacted replacements computed for the request. Included only when redaction applies.
        :type redaction_replacements: [AIGuardRedactionReplacement], optional

        :param scfw_findings: The Supply Chain Firewall verdict for the version-pinned install packages
            found in the request. Evaluation requires Supply Chain Firewall to be enabled
            for the organization and the caller to have the ``appsec_vm_read`` permission.
            Without that permission, Supply Chain Firewall evaluation is skipped; the
            AI Guard evaluation request itself is not rejected. Findings are omitted
            when Supply Chain Firewall does not produce a result.
            The recommended action combines the package outcomes.
            Confirmation support is inferred from the evaluator profile, not from a
            separate confirmation-capability flag. By default, a non-empty
            ``meta.coding_agent`` selects the coding-agent profile, which assumes the caller
            can ask for confirmation and retains WARN in ``recommended_action``.
            Omitting ``meta.coding_agent`` or setting it to an empty string selects the
            default profile, which assumes the caller cannot ask for confirmation and
            returns ALLOW instead of WARN in ``recommended_action``. Package outcomes
            still retain WARN, and BLOCK is never changed to ALLOW by this rule.
        :type scfw_findings: AIGuardScfwFindings, optional

        :param sds_findings: The sensitive data findings from the Sensitive Data Scanner. Included only when findings exist.
        :type sds_findings: [AIGuardSdsFinding], optional

        :param tag_probs: The detection confidence for each threat tag, between ``0`` and ``1``. May be null when the evaluation does not produce per-category scores.
        :type tag_probs: {str: (float,)}, none_type

        :param tags: The threat tags detected in the conversation.
        :type tags: [str]
        """
        if global_prob is not unset:
            kwargs["global_prob"] = global_prob
        if redaction_replacements is not unset:
            kwargs["redaction_replacements"] = redaction_replacements
        if scfw_findings is not unset:
            kwargs["scfw_findings"] = scfw_findings
        if sds_findings is not unset:
            kwargs["sds_findings"] = sds_findings
        super().__init__(kwargs)

        self_.action = action
        self_.is_blocking_enabled = is_blocking_enabled
        self_.reason = reason
        self_.tag_probs = tag_probs
        self_.tags = tags
