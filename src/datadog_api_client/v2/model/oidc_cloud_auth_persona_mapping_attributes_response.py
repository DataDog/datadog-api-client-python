# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.oidc_cloud_auth_claim_matcher import OIDCCloudAuthClaimMatcher


class OIDCCloudAuthPersonaMappingAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.oidc_cloud_auth_claim_matcher import OIDCCloudAuthClaimMatcher

        return {
            "account_identifier": (str,),
            "account_uuid": (str,),
            "claim_matchers": ([OIDCCloudAuthClaimMatcher],),
            "created_at": (datetime,),
            "created_by": (UUID,),
            "identity_pattern": (str,),
            "provider_id": (UUID,),
        }

    attribute_map = {
        "account_identifier": "account_identifier",
        "account_uuid": "account_uuid",
        "claim_matchers": "claim_matchers",
        "created_at": "created_at",
        "created_by": "created_by",
        "identity_pattern": "identity_pattern",
        "provider_id": "provider_id",
    }
    read_only_vars = {
        "account_identifier",
        "created_at",
        "created_by",
    }

    def __init__(
        self_,
        account_identifier: Union[str, UnsetType] = unset,
        account_uuid: Union[str, UnsetType] = unset,
        claim_matchers: Union[List[OIDCCloudAuthClaimMatcher], UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[UUID, UnsetType] = unset,
        identity_pattern: Union[str, UnsetType] = unset,
        provider_id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Stored Custom OIDC persona mapping attributes.

        :param account_identifier: Handle resolved when the mapping was created; not updated if the account handle changes.
        :type account_identifier: str, optional

        :param account_uuid: UUID of the Datadog user or service account to authenticate as.
        :type account_uuid: str, optional

        :param claim_matchers: Every claim condition must match. Supply claim_matchers or identity_pattern, but not both.
        :type claim_matchers: [OIDCCloudAuthClaimMatcher], optional

        :param created_at: Time the configuration was created.
        :type created_at: datetime, optional

        :param created_by: UUID of the user who created the configuration.
        :type created_by: UUID, optional

        :param identity_pattern: Legacy glob pattern matched against the provider identity claim. Supply this or claim_matchers, but not both. Prefer claim_matchers with exact mode for a single Kubernetes service account.
        :type identity_pattern: str, optional

        :param provider_id: UUID of the registered Custom OIDC provider.
        :type provider_id: UUID, optional
        """
        if account_identifier is not unset:
            kwargs["account_identifier"] = account_identifier
        if account_uuid is not unset:
            kwargs["account_uuid"] = account_uuid
        if claim_matchers is not unset:
            kwargs["claim_matchers"] = claim_matchers
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if identity_pattern is not unset:
            kwargs["identity_pattern"] = identity_pattern
        if provider_id is not unset:
            kwargs["provider_id"] = provider_id
        super().__init__(kwargs)
