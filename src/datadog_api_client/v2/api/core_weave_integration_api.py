# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.core_weave_cloud_integration_accounts_response import (
    CoreWeaveCloudIntegrationAccountsResponse,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_response import (
    CoreWeaveCloudIntegrationAccountResponse,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_create_request import (
    CoreWeaveCloudIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_update_request import (
    CoreWeaveCloudIntegrationAccountUpdateRequest,
)


class CoreWeaveIntegrationApi:
    """
    Manage your Datadog CoreWeave integration accounts and account resources
    directly through the Datadog API. See the
    `CoreWeave integration page <https://docs.datadoghq.com/integrations/coreweave/>`_ for
    more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_core_weave_cloud_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (CoreWeaveCloudIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/coreweave-cloud/accounts",
                "operation_id": "create_core_weave_cloud_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CoreWeaveCloudIntegrationAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_core_weave_cloud_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/coreweave-cloud/accounts/{account_id}",
                "operation_id": "delete_core_weave_cloud_integration_account",
                "http_method": "DELETE",
                "version": "v2",
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
            },
            api_client=api_client,
        )

        self._get_core_weave_cloud_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (CoreWeaveCloudIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/coreweave-cloud/accounts/{account_id}",
                "operation_id": "get_core_weave_cloud_integration_account",
                "http_method": "GET",
                "version": "v2",
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
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_core_weave_cloud_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (CoreWeaveCloudIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/coreweave-cloud/accounts",
                "operation_id": "list_core_weave_cloud_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_core_weave_cloud_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (CoreWeaveCloudIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/coreweave-cloud/accounts/{account_id}",
                "operation_id": "update_core_weave_cloud_integration_account",
                "http_method": "PATCH",
                "version": "v2",
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
                    "openapi_types": (CoreWeaveCloudIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_core_weave_cloud_integration_account(
        self,
        body: CoreWeaveCloudIntegrationAccountCreateRequest,
    ) -> CoreWeaveCloudIntegrationAccountResponse:
        """Create a CoreWeave integration account.

        Create a CoreWeave integration account.

        :type body: CoreWeaveCloudIntegrationAccountCreateRequest
        :rtype: CoreWeaveCloudIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_core_weave_cloud_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_core_weave_cloud_integration_account(
        self,
        account_id: str,
    ) -> None:
        """Delete a CoreWeave integration account.

        Delete a CoreWeave integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_core_weave_cloud_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_core_weave_cloud_integration_account(
        self,
        account_id: str,
    ) -> CoreWeaveCloudIntegrationAccountResponse:
        """Get a CoreWeave integration account.

        Get a CoreWeave integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: CoreWeaveCloudIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_core_weave_cloud_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_core_weave_cloud_integration_accounts(
        self,
    ) -> CoreWeaveCloudIntegrationAccountsResponse:
        """List CoreWeave integration accounts.

        List CoreWeave integration accounts.

        :rtype: CoreWeaveCloudIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_core_weave_cloud_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_core_weave_cloud_integration_account(
        self,
        account_id: str,
        body: CoreWeaveCloudIntegrationAccountUpdateRequest,
    ) -> CoreWeaveCloudIntegrationAccountResponse:
        """Update a CoreWeave integration account.

        Update a CoreWeave integration account. Only the fields provided are changed.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: CoreWeaveCloudIntegrationAccountUpdateRequest
        :rtype: CoreWeaveCloudIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_core_weave_cloud_integration_account_endpoint.call_with_http_info(**kwargs)
