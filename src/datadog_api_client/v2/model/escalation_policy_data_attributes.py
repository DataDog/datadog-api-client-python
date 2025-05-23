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


class EscalationPolicyDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "resolve_page_on_policy_end": (bool,),
            "retries": (int,),
        }

    attribute_map = {
        "name": "name",
        "resolve_page_on_policy_end": "resolve_page_on_policy_end",
        "retries": "retries",
    }

    def __init__(
        self_,
        name: str,
        resolve_page_on_policy_end: Union[bool, UnsetType] = unset,
        retries: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines the main attributes of an escalation policy, such as its name and behavior on policy end.

        :param name: Specifies the name of the escalation policy.
        :type name: str

        :param resolve_page_on_policy_end: Indicates whether the page is automatically resolved when the policy ends.
        :type resolve_page_on_policy_end: bool, optional

        :param retries: Specifies how many times the escalation sequence is retried if there is no response.
        :type retries: int, optional
        """
        if resolve_page_on_policy_end is not unset:
            kwargs["resolve_page_on_policy_end"] = resolve_page_on_policy_end
        if retries is not unset:
            kwargs["retries"] = retries
        super().__init__(kwargs)

        self_.name = name
