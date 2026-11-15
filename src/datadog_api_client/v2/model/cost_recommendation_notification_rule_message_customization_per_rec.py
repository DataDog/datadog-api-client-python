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


class CostRecommendationNotificationRuleMessageCustomizationPerRec(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "effort": (bool,),
            "risk": (bool,),
            "why": (bool,),
        }

    attribute_map = {
        "effort": "effort",
        "risk": "risk",
        "why": "why",
    }

    def __init__(
        self_,
        effort: Union[bool, UnsetType] = unset,
        risk: Union[bool, UnsetType] = unset,
        why: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        What each recommendation in the digest shows.

        :param effort: Whether each recommendation shows its effort.
        :type effort: bool, optional

        :param risk: Whether each recommendation shows its risk.
        :type risk: bool, optional

        :param why: Whether each recommendation shows why it was made.
        :type why: bool, optional
        """
        if effort is not unset:
            kwargs["effort"] = effort
        if risk is not unset:
            kwargs["risk"] = risk
        if why is not unset:
            kwargs["why"] = why
        super().__init__(kwargs)
