# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect


class StatusPageEmailAccessPolicyDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect

        return {
            "created_at": (datetime,),
            "effect": (ExecutionPolicyEffect,),
            "pattern": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "effect": "effect",
        "pattern": "pattern",
    }

    def __init__(self_, created_at: datetime, effect: ExecutionPolicyEffect, pattern: str, **kwargs):
        """
        Attributes of a status page email access policy.

        :param created_at: Timestamp of when the email access policy was created.
        :type created_at: datetime

        :param effect: Whether the policy allows or denies matching actions.
        :type effect: ExecutionPolicyEffect

        :param pattern: The email address pattern matched by the policy.
        :type pattern: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.effect = effect
        self_.pattern = pattern
