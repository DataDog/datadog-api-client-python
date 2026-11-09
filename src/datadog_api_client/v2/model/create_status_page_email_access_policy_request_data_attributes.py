# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.access_policy_effect import AccessPolicyEffect


class CreateStatusPageEmailAccessPolicyRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.access_policy_effect import AccessPolicyEffect

        return {
            "effect": (AccessPolicyEffect,),
            "pattern": (str,),
        }

    attribute_map = {
        "effect": "effect",
        "pattern": "pattern",
    }

    def __init__(self_, effect: AccessPolicyEffect, pattern: str, **kwargs):
        """
        Attributes for creating a status page email access policy.

        :param effect: The effect applied when an email address matches the policy. Deny policies take precedence over allow policies.
        :type effect: AccessPolicyEffect

        :param pattern: The email address pattern matched by the policy. Supports an exact address ( ``user@example.com`` ), all addresses in a domain ( ``@example.com`` ), or all addresses in subdomains ( ``@*.example.com`` ).
        :type pattern: str
        """
        super().__init__(kwargs)

        self_.effect = effect
        self_.pattern = pattern
