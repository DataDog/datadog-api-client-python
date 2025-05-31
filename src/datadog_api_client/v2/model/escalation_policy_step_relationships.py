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
    from datadog_api_client.v2.model.escalation_targets import EscalationTargets


class EscalationPolicyStepRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_targets import EscalationTargets

        return {
            "targets": (EscalationTargets,),
        }

    attribute_map = {
        "targets": "targets",
    }

    def __init__(self_, targets: Union[EscalationTargets, UnsetType] = unset, **kwargs):
        """
        Represents the relationship of an escalation policy step to its targets.

        :param targets: A list of escalation targets for a step
        :type targets: EscalationTargets, optional
        """
        if targets is not unset:
            kwargs["targets"] = targets
        super().__init__(kwargs)
