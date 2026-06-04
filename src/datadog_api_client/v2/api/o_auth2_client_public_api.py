# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UUID,
)
from datadog_api_client.v2.model.o_auth2_well_known_sites_response import OAuth2WellKnownSitesResponse
from datadog_api_client.v2.model.o_auth_scopes_restriction_response import OAuthScopesRestrictionResponse
from datadog_api_client.v2.model.upsert_o_auth_scopes_restriction_request import UpsertOAuthScopesRestrictionRequest
from datadog_api_client.v2.model.o_auth_client_registration_response import OAuthClientRegistrationResponse
from datadog_api_client.v2.model.o_auth_client_registration_request import OAuthClientRegistrationRequest


class OAuth2ClientPublicApi:
    """
    Configure OAuth2 clients for Datadog.
    Supports RFC 7591 Dynamic Client Registration and management of OAuth2 client scopes restrictions.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._delete_scopes_restriction_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/oauth2/clients/{client_uuid}/scopes_restriction",
                "operation_id": "delete_scopes_restriction",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "client_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "client_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_o_auth2_well_known_sites_endpoint = _Endpoint(
            settings={
                "response_type": (OAuth2WellKnownSitesResponse,),
                "auth": [],
                "endpoint_path": "/api/v2/oauth2/.well-known/sites",
                "operation_id": "get_o_auth2_well_known_sites",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_scopes_restriction_endpoint = _Endpoint(
            settings={
                "response_type": (OAuthScopesRestrictionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/oauth2/clients/{client_uuid}/scopes_restriction",
                "operation_id": "get_scopes_restriction",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "client_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "client_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._register_o_auth_client_endpoint = _Endpoint(
            settings={
                "response_type": (OAuthClientRegistrationResponse,),
                "auth": [],
                "endpoint_path": "/api/v2/oauth2/register",
                "operation_id": "register_o_auth_client",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OAuthClientRegistrationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upsert_scopes_restriction_endpoint = _Endpoint(
            settings={
                "response_type": (OAuthScopesRestrictionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/oauth2/clients/{client_uuid}/scopes_restriction",
                "operation_id": "upsert_scopes_restriction",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "client_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "client_uuid",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpsertOAuthScopesRestrictionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def delete_scopes_restriction(
        self,
        client_uuid: UUID,
    ) -> None:
        """Delete an OAuth2 client scopes restriction.

        Delete the scopes restriction configured for the OAuth2 client.

        :param client_uuid: UUID of the OAuth2 client.
        :type client_uuid: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["client_uuid"] = client_uuid

        return self._delete_scopes_restriction_endpoint.call_with_http_info(**kwargs)

    def get_o_auth2_well_known_sites(
        self,
    ) -> OAuth2WellKnownSitesResponse:
        """Get OAuth2 well-known sites.

        Retrieve the list of public OAuth2 sites available for the current environment. This endpoint is used for OAuth2 discovery and returns sites where users can authenticate.

        :rtype: OAuth2WellKnownSitesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_o_auth2_well_known_sites_endpoint.call_with_http_info(**kwargs)

    def get_scopes_restriction(
        self,
        client_uuid: UUID,
    ) -> OAuthScopesRestrictionResponse:
        """Get an OAuth2 client scopes restriction.

        Get the scopes restriction configured for the OAuth2 client.

        :param client_uuid: UUID of the OAuth2 client.
        :type client_uuid: UUID
        :rtype: OAuthScopesRestrictionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["client_uuid"] = client_uuid

        return self._get_scopes_restriction_endpoint.call_with_http_info(**kwargs)

    def register_o_auth_client(
        self,
        body: OAuthClientRegistrationRequest,
    ) -> OAuthClientRegistrationResponse:
        """Register an OAuth2 client.

        Register an OAuth2 client using the Dynamic Client Registration protocol defined in RFC 7591.

        :type body: OAuthClientRegistrationRequest
        :rtype: OAuthClientRegistrationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._register_o_auth_client_endpoint.call_with_http_info(**kwargs)

    def upsert_scopes_restriction(
        self,
        client_uuid: UUID,
        body: UpsertOAuthScopesRestrictionRequest,
    ) -> OAuthScopesRestrictionResponse:
        """Upsert an OAuth2 client scopes restriction.

        Create or update the scopes restriction configured for the OAuth2 client.

        :param client_uuid: UUID of the OAuth2 client.
        :type client_uuid: UUID
        :type body: UpsertOAuthScopesRestrictionRequest
        :rtype: OAuthScopesRestrictionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["client_uuid"] = client_uuid

        kwargs["body"] = body

        return self._upsert_scopes_restriction_endpoint.call_with_http_info(**kwargs)
