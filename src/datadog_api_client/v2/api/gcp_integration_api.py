# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.sts_enabled_account_data import STSEnabledAccountData
from datadog_api_client.v2.model.account_creation_response import AccountCreationResponse
from datadog_api_client.v2.model.service_account_to_be_created_data import ServiceAccountToBeCreatedData
from datadog_api_client.v2.model.account_patch_body import AccountPatchBody
from datadog_api_client.v2.model.delegate_creation_response import DelegateCreationResponse


class GCPIntegrationApi:
    """
    Configure your Datadog-Google Cloud Platform (GCP) integration directly
    through the Datadog API. Read more about the `Datadog-Google Cloud Platform integration <https://docs.datadoghq.com/integrations/google_cloud_platform>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_gcpsts_accounts_v2_endpoint = _Endpoint(
            settings={
                "response_type": (AccountCreationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/gcp/accounts",
                "operation_id": "create_gcpsts_accounts_v2",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ServiceAccountToBeCreatedData,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_gcpsts_accounts_v2_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/gcp/accounts/{account_id}",
                "operation_id": "delete_gcpsts_accounts_v2",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_delegate_v2_endpoint = _Endpoint(
            settings={
                "response_type": (DelegateCreationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/gcp/sts_delegate",
                "operation_id": "get_delegate_v2",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "openapi_types": (dict,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_gcpsts_accounts_v2_endpoint = _Endpoint(
            settings={
                "response_type": (STSEnabledAccountData,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/gcp/accounts",
                "operation_id": "list_gcpsts_accounts_v2",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._make_delegate_v2_endpoint = _Endpoint(
            settings={
                "response_type": (DelegateCreationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/gcp/sts_delegate",
                "operation_id": "make_delegate_v2",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "openapi_types": (dict,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_gcpsts_accounts_v2_endpoint = _Endpoint(
            settings={
                "response_type": (AccountPatchBody,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/gcp/accounts/{account_id}",
                "operation_id": "update_gcpsts_accounts_v2",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AccountPatchBody,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_gcpsts_accounts_v2(
        self,
        body: ServiceAccountToBeCreatedData,
    ) -> AccountCreationResponse:
        """Create a new entry for your service account.

        Create a new entry within Datadog for your STS enabled service account.

        :type body: ServiceAccountToBeCreatedData
        :rtype: AccountCreationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_gcpsts_accounts_v2_endpoint.call_with_http_info(**kwargs)

    def delete_gcpsts_accounts_v2(
        self,
        account_id: str,
    ) -> None:
        """Delete an STS enabled GCP Account.

        Delete an STS enabled GCP account from within Datadog.

        :param account_id: Your GCP STS enabled service account's unique ID.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_gcpsts_accounts_v2_endpoint.call_with_http_info(**kwargs)

    def get_delegate_v2(
        self,
        *,
        body: Union[dict, UnsetType] = unset,
    ) -> DelegateCreationResponse:
        """List delegate account.

        List your Datadog-GCP STS delegate account configured in your Datadog account.

        :param body: Get a Datadog GCP STS delegate account.
        :type body: dict, optional
        :rtype: DelegateCreationResponse
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        return self._get_delegate_v2_endpoint.call_with_http_info(**kwargs)

    def list_gcpsts_accounts_v2(
        self,
    ) -> STSEnabledAccountData:
        """List all GCP STS-enabled service accounts.

        List all GCP STS-enabled service accounts configured in your Datadog account.

        :rtype: STSEnabledAccountData
        """
        kwargs: Dict[str, Any] = {}
        return self._list_gcpsts_accounts_v2_endpoint.call_with_http_info(**kwargs)

    def make_delegate_v2(
        self,
        *,
        body: Union[dict, UnsetType] = unset,
    ) -> DelegateCreationResponse:
        """Create a Datadog GCP principal.

        Create a Datadog GCP principal.

        :param body: Create a delegate service account within Datadog.
        :type body: dict, optional
        :rtype: DelegateCreationResponse
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        return self._make_delegate_v2_endpoint.call_with_http_info(**kwargs)

    def update_gcpsts_accounts_v2(
        self,
        account_id: str,
        body: AccountPatchBody,
    ) -> AccountPatchBody:
        """Update STS Service Account.

        Update an STS enabled service account.

        :param account_id: Your GCP STS enabled service account's unique ID.
        :type account_id: str
        :type body: AccountPatchBody
        :rtype: AccountPatchBody
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_gcpsts_accounts_v2_endpoint.call_with_http_info(**kwargs)
