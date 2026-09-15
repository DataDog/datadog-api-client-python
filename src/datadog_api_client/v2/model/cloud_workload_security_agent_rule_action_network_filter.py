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


class CloudWorkloadSecurityAgentRuleActionNetworkFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "filter": (str,),
            "policy": (str,),
            "scope": (str,),
        }

    attribute_map = {
        "filter": "filter",
        "policy": "policy",
        "scope": "scope",
    }

    def __init__(
        self_,
        filter: Union[str, UnsetType] = unset,
        policy: Union[str, UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The network filter action applied on the network traffic matching the rule.

        :param filter: The filter expression of the network filter action.
        :type filter: str, optional

        :param policy: The policy of the network filter action.
        :type policy: str, optional

        :param scope: The scope of the network filter action.
        :type scope: str, optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if policy is not unset:
            kwargs["policy"] = policy
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)
