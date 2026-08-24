# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.elastic_cloud_integration_accounts_response import (
    ElasticCloudIntegrationAccountsResponse,
)
from datadog_api_client.v2.model.elastic_cloud_integration_account_response import (
    ElasticCloudIntegrationAccountResponse,
)
from datadog_api_client.v2.model.elastic_cloud_integration_account_create_request import (
    ElasticCloudIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.elastic_cloud_integration_account_update_request import (
    ElasticCloudIntegrationAccountUpdateRequest,
)


class ElasticCloudIntegrationAccountsApi:
    """
    Manage your Datadog Elastic Cloud integration accounts directly through the Datadog API.
    Create, update, and delete accounts, configure authentication and settings, and
    enable or disable dataflows such as cluster metrics, index stats, shard stats,
    pending tasks, and snapshot lifecycle management stats. See the
    `Elastic Cloud integration page <https://docs.datadoghq.com/integrations/elastic-cloud/>`_ for
    more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_elastic_cloud_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (ElasticCloudIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/elastic-cloud/accounts",
                "operation_id": "create_elastic_cloud_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ElasticCloudIntegrationAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_elastic_cloud_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/elastic-cloud/accounts/{account_id}",
                "operation_id": "delete_elastic_cloud_integration_account",
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

        self._get_elastic_cloud_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (ElasticCloudIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/elastic-cloud/accounts/{account_id}",
                "operation_id": "get_elastic_cloud_integration_account",
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

        self._list_elastic_cloud_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (ElasticCloudIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/elastic-cloud/accounts",
                "operation_id": "list_elastic_cloud_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_elastic_cloud_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (ElasticCloudIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/elastic-cloud/accounts/{account_id}",
                "operation_id": "update_elastic_cloud_integration_account",
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
                    "openapi_types": (ElasticCloudIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_elastic_cloud_integration_account(
        self,
        body: ElasticCloudIntegrationAccountCreateRequest,
    ) -> ElasticCloudIntegrationAccountResponse:
        """Create an Elastic Cloud integration account.

        Create an Elastic Cloud integration account.

        :type body: ElasticCloudIntegrationAccountCreateRequest
        :rtype: ElasticCloudIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_elastic_cloud_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_elastic_cloud_integration_account(
        self,
        account_id: str,
    ) -> None:
        """Delete an Elastic Cloud integration account.

        Delete an Elastic Cloud integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_elastic_cloud_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_elastic_cloud_integration_account(
        self,
        account_id: str,
    ) -> ElasticCloudIntegrationAccountResponse:
        """Get an Elastic Cloud integration account.

        Get an Elastic Cloud integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: ElasticCloudIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_elastic_cloud_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_elastic_cloud_integration_accounts(
        self,
    ) -> ElasticCloudIntegrationAccountsResponse:
        """List Elastic Cloud integration accounts.

        List Elastic Cloud integration accounts.

        :rtype: ElasticCloudIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_elastic_cloud_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_elastic_cloud_integration_account(
        self,
        account_id: str,
        body: ElasticCloudIntegrationAccountUpdateRequest,
    ) -> ElasticCloudIntegrationAccountResponse:
        """Update an Elastic Cloud integration account.

        Update an Elastic Cloud integration account. Only the fields provided are changed.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: ElasticCloudIntegrationAccountUpdateRequest
        :rtype: ElasticCloudIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_elastic_cloud_integration_account_endpoint.call_with_http_info(**kwargs)
