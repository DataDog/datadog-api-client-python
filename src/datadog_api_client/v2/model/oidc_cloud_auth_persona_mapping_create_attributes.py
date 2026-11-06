# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.oidc_cloud_auth_claim_matcher_create import OIDCCloudAuthClaimMatcherCreate


class OIDCCloudAuthPersonaMappingCreateAttributes(ModelNormal):
    validations = {
        "identity_pattern": {
            "max_length": 500,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.oidc_cloud_auth_claim_matcher_create import OIDCCloudAuthClaimMatcherCreate

        return {
            "account_uuid": (str,),
            "claim_matchers": ([OIDCCloudAuthClaimMatcherCreate],),
            "identity_pattern": (str,),
            "provider_id": (UUID,),
        }

    attribute_map = {
        "account_uuid": "account_uuid",
        "claim_matchers": "claim_matchers",
        "identity_pattern": "identity_pattern",
        "provider_id": "provider_id",
    }

    def __init__(
        self_,
        account_uuid: str,
        provider_id: UUID,
        claim_matchers: Union[List[OIDCCloudAuthClaimMatcherCreate], UnsetType] = unset,
        identity_pattern: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a Custom OIDC persona mapping.

        :param account_uuid: UUID of the Datadog user or service account to authenticate as.
        :type account_uuid: str

        :param claim_matchers: Every claim condition must match. Supply claim_matchers or identity_pattern, but not both.
        :type claim_matchers: [OIDCCloudAuthClaimMatcherCreate], optional

        :param identity_pattern: Legacy glob pattern, limited to 500 UTF-8 bytes when creating a mapping, matched against the provider identity claim. Supply this or claim_matchers, but not both. Prefer claim_matchers with exact mode for a single Kubernetes service account.
        :type identity_pattern: str, optional

        :param provider_id: UUID of the registered Custom OIDC provider.
        :type provider_id: UUID
        """
        if claim_matchers is not unset:
            kwargs["claim_matchers"] = claim_matchers
        if identity_pattern is not unset:
            kwargs["identity_pattern"] = identity_pattern
        super().__init__(kwargs)

        self_.account_uuid = account_uuid
        self_.provider_id = provider_id
