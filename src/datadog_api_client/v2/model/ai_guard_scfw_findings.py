# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_guard_scfw_package_finding import AIGuardScfwPackageFinding
    from datadog_api_client.v2.model.ai_guard_scfw_outcome import AIGuardScfwOutcome


class AIGuardScfwFindings(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_scfw_package_finding import AIGuardScfwPackageFinding
        from datadog_api_client.v2.model.ai_guard_scfw_outcome import AIGuardScfwOutcome

        return {
            "packages": ([AIGuardScfwPackageFinding],),
            "recommended_action": (AIGuardScfwOutcome,),
        }

    attribute_map = {
        "packages": "packages",
        "recommended_action": "recommended_action",
    }

    def __init__(
        self_,
        recommended_action: AIGuardScfwOutcome,
        packages: Union[List[AIGuardScfwPackageFinding], UnsetType] = unset,
        **kwargs,
    ):
        """
        The Supply Chain Firewall verdict for the version-pinned install packages
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

        :param packages: The packages the firewall evaluated, ``ALLOW`` ones included.
        :type packages: [AIGuardScfwPackageFinding], optional

        :param recommended_action: The Supply Chain Firewall outcome for a package, a matched rule, or the whole request.
        :type recommended_action: AIGuardScfwOutcome
        """
        if packages is not unset:
            kwargs["packages"] = packages
        super().__init__(kwargs)

        self_.recommended_action = recommended_action
