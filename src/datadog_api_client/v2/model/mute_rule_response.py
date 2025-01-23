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
    from datadog_api_client.v2.model.mute_rule import MuteRule


class MuteRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_rule import MuteRule

        return {
            "data": (MuteRule,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[MuteRule, UnsetType] = unset, **kwargs):
        """
        Response object which includes a mute rule.

        :param data: Mute rules are used to proactively filter out known false positives or accepted risks.
            A mute rule is composed of a rule UUID, a rule type, and the rule attributes. All fields are required.
        :type data: MuteRule, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
