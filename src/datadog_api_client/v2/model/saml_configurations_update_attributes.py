# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class SamlConfigurationsUpdateAttributes(ModelNormal):
    validations = {
        "default_role_uuids": {
            "max_items": 1,
            "min_items": 1,
        },
        "jit_domains": {
            "max_items": 50,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "default_role_uuids": ([UUID],),
            "jit_domains": ([str],),
        }

    attribute_map = {
        "default_role_uuids": "default_role_uuids",
        "jit_domains": "jit_domains",
    }

    def __init__(self_, default_role_uuids: List[UUID], jit_domains: List[str], **kwargs):
        """
        Attributes for updating SAML preferences.

        :param default_role_uuids: List of role UUIDs to assign to JIT-provisioned users. Exactly 1 role is required.
        :type default_role_uuids: [UUID]

        :param jit_domains: List of domains for Just-In-Time user provisioning. Maximum 50 domains.
            Each domain must be between 1 and 256 characters.
        :type jit_domains: [str]
        """
        super().__init__(kwargs)

        self_.default_role_uuids = default_role_uuids
        self_.jit_domains = jit_domains
