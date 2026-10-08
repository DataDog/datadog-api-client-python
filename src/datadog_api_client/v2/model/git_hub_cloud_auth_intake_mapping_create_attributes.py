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
    from datadog_api_client.v2.model.git_hub_oidc_claim_patterns import GitHubOIDCClaimPatterns


class GitHubCloudAuthIntakeMappingCreateAttributes(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.git_hub_oidc_claim_patterns import GitHubOIDCClaimPatterns

        return {
            "claim_matchers": (GitHubOIDCClaimPatterns,),
        }

    attribute_map = {
        "claim_matchers": "claim_matchers",
    }

    def __init__(self_, claim_matchers: GitHubOIDCClaimPatterns, **kwargs):
        """
        Attributes for creating a GitHub cloud authentication intake mapping

        :param claim_matchers: GitHub Actions OIDC claims to match against. Each field is a regular expression.
            The ``sub`` claim is required; all other claims are optional. A token matches only when
            all provided patterns match simultaneously (AND semantics).
        :type claim_matchers: GitHubOIDCClaimPatterns
        """
        super().__init__(kwargs)

        self_.claim_matchers = claim_matchers
