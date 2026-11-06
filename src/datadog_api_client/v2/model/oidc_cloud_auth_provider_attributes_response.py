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
    from datadog_api_client.v2.model.oidc_cloud_auth_discovery_type import OIDCCloudAuthDiscoveryType
    from datadog_api_client.v2.model.oidc_cloud_auth_org_uuid_source import OIDCCloudAuthOrgUUIDSource
    from datadog_api_client.v2.model.oidc_cloud_auth_claim_matcher import OIDCCloudAuthClaimMatcher


class OIDCCloudAuthProviderAttributesResponse(ModelNormal):
    validations = {
        "audiences": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.oidc_cloud_auth_discovery_type import OIDCCloudAuthDiscoveryType
        from datadog_api_client.v2.model.oidc_cloud_auth_org_uuid_source import OIDCCloudAuthOrgUUIDSource
        from datadog_api_client.v2.model.oidc_cloud_auth_claim_matcher import OIDCCloudAuthClaimMatcher

        return {
            "audiences": ([str],),
            "created_at": (datetime,),
            "created_by": (UUID,),
            "discovery_type": (OIDCCloudAuthDiscoveryType,),
            "identity_claim_name": (str,),
            "issuer_url": (str,),
            "jwks_url": (str,),
            "org_uuid_claim_name": (str,),
            "org_uuid_source": (OIDCCloudAuthOrgUUIDSource,),
            "provider_name": (str,),
            "required_claims": ([OIDCCloudAuthClaimMatcher],),
        }

    attribute_map = {
        "audiences": "audiences",
        "created_at": "created_at",
        "created_by": "created_by",
        "discovery_type": "discovery_type",
        "identity_claim_name": "identity_claim_name",
        "issuer_url": "issuer_url",
        "jwks_url": "jwks_url",
        "org_uuid_claim_name": "org_uuid_claim_name",
        "org_uuid_source": "org_uuid_source",
        "provider_name": "provider_name",
        "required_claims": "required_claims",
    }
    read_only_vars = {
        "created_at",
        "created_by",
    }

    def __init__(
        self_,
        audiences: Union[List[str], UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[UUID, UnsetType] = unset,
        discovery_type: Union[OIDCCloudAuthDiscoveryType, UnsetType] = unset,
        identity_claim_name: Union[str, UnsetType] = unset,
        issuer_url: Union[str, UnsetType] = unset,
        jwks_url: Union[str, UnsetType] = unset,
        org_uuid_claim_name: Union[str, UnsetType] = unset,
        org_uuid_source: Union[OIDCCloudAuthOrgUUIDSource, UnsetType] = unset,
        provider_name: Union[str, UnsetType] = unset,
        required_claims: Union[List[OIDCCloudAuthClaimMatcher], UnsetType] = unset,
        **kwargs,
    ):
        """
        Stored Custom OIDC provider attributes.

        :param audiences: Expected token audiences. At least one audience is required. When ``org_uuid_source`` is ``aud`` , include datadog/{org_uuid} for the organization creating the provider.
        :type audiences: [str], optional

        :param created_at: Time the configuration was created.
        :type created_at: datetime, optional

        :param created_by: UUID of the user who created the configuration.
        :type created_by: UUID, optional

        :param discovery_type: How the signing keys are discovered.
        :type discovery_type: OIDCCloudAuthDiscoveryType, optional

        :param identity_claim_name: Claim used by legacy identity_pattern mappings and in identity logs.
        :type identity_claim_name: str, optional

        :param issuer_url: HTTPS issuer URL that must match the token issuer. For oidc_discovery, signing keys are located through the issuer discovery document.
        :type issuer_url: str, optional

        :param jwks_url: HTTPS JSON Web Key Set URL. Required when ``discovery_type`` is ``direct_jwks``.
        :type jwks_url: str, optional

        :param org_uuid_claim_name: Optional name of the token claim containing the Datadog organization UUID.
        :type org_uuid_claim_name: str, optional

        :param org_uuid_source: Source of the organization UUID in the signed token. The ``aud`` source accepts a datadog/{org_uuid} audience.
        :type org_uuid_source: OIDCCloudAuthOrgUUIDSource, optional

        :param provider_name: Name identifying the provider within the organization.
        :type provider_name: str, optional

        :param required_claims: Claim matchers required for every token from this provider, in addition to the persona mapping matchers. Shared issuers can require an exact tenant claim.
        :type required_claims: [OIDCCloudAuthClaimMatcher], optional
        """
        if audiences is not unset:
            kwargs["audiences"] = audiences
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if discovery_type is not unset:
            kwargs["discovery_type"] = discovery_type
        if identity_claim_name is not unset:
            kwargs["identity_claim_name"] = identity_claim_name
        if issuer_url is not unset:
            kwargs["issuer_url"] = issuer_url
        if jwks_url is not unset:
            kwargs["jwks_url"] = jwks_url
        if org_uuid_claim_name is not unset:
            kwargs["org_uuid_claim_name"] = org_uuid_claim_name
        if org_uuid_source is not unset:
            kwargs["org_uuid_source"] = org_uuid_source
        if provider_name is not unset:
            kwargs["provider_name"] = provider_name
        if required_claims is not unset:
            kwargs["required_claims"] = required_claims
        super().__init__(kwargs)
