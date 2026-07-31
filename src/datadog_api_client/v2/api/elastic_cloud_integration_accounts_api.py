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
from datadog_api_client.v2.model.elastic_cloud_interface_id import ElasticCloudInterfaceId
from datadog_api_client.v2.model.elastic_cloud_integration_account_response import (
    ElasticCloudIntegrationAccountResponse,
)
from datadog_api_client.v2.model.elastic_cloud_integration_account_request import ElasticCloudIntegrationAccountRequest
from datadog_api_client.v2.model.elastic_cloud_integration_account_update_request import (
    ElasticCloudIntegrationAccountUpdateRequest,
)


class ElasticCloudIntegrationAccountsApi:
    """
    Manage Elastic Cloud accounts for the Elastic Cloud integration, served by the Account Management Service (AMS). The account payload is strongly typed to Elastic Cloud; the supported interfaces (monitoring and Cloud Cost Management) are modeled as a nested union.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_elastic_cloud_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (ElasticCloudIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/elastic-cloud/interfaces/{interface_id}/accounts",
                "operation_id": "create_elastic_cloud_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "interface_id": {
                    "required": True,
                    "openapi_types": (ElasticCloudInterfaceId,),
                    "attribute": "interface_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ElasticCloudIntegrationAccountRequest,),
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
                "endpoint_path": "/api/v2/integrations/elastic-cloud/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "delete_elastic_cloud_integration_account",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "interface_id": {
                    "required": True,
                    "openapi_types": (ElasticCloudInterfaceId,),
                    "attribute": "interface_id",
                    "location": "path",
                },
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
                "endpoint_path": "/api/v2/integrations/elastic-cloud/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "get_elastic_cloud_integration_account",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "interface_id": {
                    "required": True,
                    "openapi_types": (ElasticCloudInterfaceId,),
                    "attribute": "interface_id",
                    "location": "path",
                },
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
                "endpoint_path": "/api/v2/integrations/elastic-cloud/interfaces/{interface_id}/accounts",
                "operation_id": "list_elastic_cloud_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "interface_id": {
                    "required": True,
                    "openapi_types": (ElasticCloudInterfaceId,),
                    "attribute": "interface_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_elastic_cloud_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (ElasticCloudIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/elastic-cloud/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "update_elastic_cloud_integration_account",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "interface_id": {
                    "required": True,
                    "openapi_types": (ElasticCloudInterfaceId,),
                    "attribute": "interface_id",
                    "location": "path",
                },
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
        interface_id: ElasticCloudInterfaceId,
        body: ElasticCloudIntegrationAccountRequest,
    ) -> ElasticCloudIntegrationAccountResponse:
        """Create an Elastic Cloud integration account.

        Create an Elastic Cloud integration account for a given interface.

        :param interface_id: Selects the Elastic Cloud interface (source-type). Supported values: ``elastic-cloud`` , ``elastic-cloud-ccm``.
        :type interface_id: ElasticCloudInterfaceId
        :type body: ElasticCloudIntegrationAccountRequest
        :rtype: ElasticCloudIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["interface_id"] = interface_id

        kwargs["body"] = body

        return self._create_elastic_cloud_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_elastic_cloud_integration_account(
        self,
        interface_id: ElasticCloudInterfaceId,
        account_id: str,
    ) -> None:
        """Delete an Elastic Cloud integration account.

        Delete an Elastic Cloud integration account.

        :param interface_id: Selects the Elastic Cloud interface (source-type). Supported values: ``elastic-cloud`` , ``elastic-cloud-ccm``.
        :type interface_id: ElasticCloudInterfaceId
        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        return self._delete_elastic_cloud_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_elastic_cloud_integration_account(
        self,
        interface_id: ElasticCloudInterfaceId,
        account_id: str,
    ) -> ElasticCloudIntegrationAccountResponse:
        """Get an Elastic Cloud integration account.

        Get a single Elastic Cloud integration account.

        :param interface_id: Selects the Elastic Cloud interface (source-type). Supported values: ``elastic-cloud`` , ``elastic-cloud-ccm``.
        :type interface_id: ElasticCloudInterfaceId
        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: ElasticCloudIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        return self._get_elastic_cloud_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_elastic_cloud_integration_accounts(
        self,
        interface_id: ElasticCloudInterfaceId,
    ) -> ElasticCloudIntegrationAccountsResponse:
        """List Elastic Cloud integration accounts.

        List the Elastic Cloud integration accounts for a given interface.

        :param interface_id: Selects the Elastic Cloud interface (source-type). Supported values: ``elastic-cloud`` , ``elastic-cloud-ccm``.
        :type interface_id: ElasticCloudInterfaceId
        :rtype: ElasticCloudIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["interface_id"] = interface_id

        return self._list_elastic_cloud_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_elastic_cloud_integration_account(
        self,
        interface_id: ElasticCloudInterfaceId,
        account_id: str,
        body: ElasticCloudIntegrationAccountUpdateRequest,
    ) -> ElasticCloudIntegrationAccountResponse:
        """Update an Elastic Cloud integration account.

        Update an Elastic Cloud integration account. The update is a partial merge: only the fields provided are changed, so a name-only or settings-only update does not need to resend the full payload or write-only credentials.

        :param interface_id: Selects the Elastic Cloud interface (source-type). Supported values: ``elastic-cloud`` , ``elastic-cloud-ccm``.
        :type interface_id: ElasticCloudInterfaceId
        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: ElasticCloudIntegrationAccountUpdateRequest
        :rtype: ElasticCloudIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_elastic_cloud_integration_account_endpoint.call_with_http_info(**kwargs)
