# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AIGuardConfidenceThreshold(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (float,)

    @cached_property
    def openapi_types(_):
        return {
            "flagging_global": (float,),
        }

    attribute_map = {
        "flagging_global": "flagging_global",
    }

    def __init__(self_, flagging_global: Union[float, UnsetType] = unset, **kwargs):
        """
        Request-level confidence threshold override. ``flagging_global`` is the global
        threshold applied to every threat category. Any other property is a
        per-category override keyed by an AI Guard threat tag; per-category values
        take precedence over ``flagging_global`` , and categories without an entry fall
        back to it. When this object omits flagging_global, the fallback is ``0.5``.
        Recognized category keys include policy-evasion, indirect-prompt-injection,
        system-and-capability-discovery, credential-access, sensitive-data-collection,
        privilege-escalation, malicious-execution, private-network-target,
        destructive-or-resource-abuse, tool-abuse, poisoning-or-persistence, and
        ``data-exfiltration``. Unknown category keys are ignored.

        :param flagging_global: The global confidence threshold applied to categories without a specific override.
        :type flagging_global: float, optional
        """
        if flagging_global is not unset:
            kwargs["flagging_global"] = flagging_global
        super().__init__(kwargs)
