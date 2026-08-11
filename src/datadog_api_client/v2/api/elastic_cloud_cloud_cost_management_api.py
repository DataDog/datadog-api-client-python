# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.elastic_cloud_ccm_accounts_response import ElasticCloudCcmAccountsResponse
from datadog_api_client.v2.model.elastic_cloud_ccm_account_response import ElasticCloudCcmAccountResponse
from datadog_api_client.v2.model.elastic_cloud_ccm_account_request import ElasticCloudCcmAccountRequest
from datadog_api_client.v2.model.elastic_cloud_ccm_account_update_request import ElasticCloudCcmAccountUpdateRequest


class ElasticCloudCloudCostManagementApi:
    """
    Manage Elastic Cloud accounts for the Cloud Cost Management interface ( ``elastic-cloud-ccm`` ), served by the Account Management Service (AMS). Concrete, strongly typed CRUD operations for the Cloud Cost Management interface.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_elastic_cloud_ccm_account_endpoint = _Endpoint(
            settings={
                "response_type": (ElasticCloudCcmAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/elastic-cloud/interfaces/elastic-cloud-ccm/accounts",
                "operation_id": "create_elastic_cloud_ccm_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ElasticCloudCcmAccountRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_elastic_cloud_ccm_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/elastic-cloud/interfaces/elastic-cloud-ccm/accounts/{account_id}",
                "operation_id": "delete_elastic_cloud_ccm_account",
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

        self._get_elastic_cloud_ccm_account_endpoint = _Endpoint(
            settings={
                "response_type": (ElasticCloudCcmAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/elastic-cloud/interfaces/elastic-cloud-ccm/accounts/{account_id}",
                "operation_id": "get_elastic_cloud_ccm_account",
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

        self._list_elastic_cloud_ccm_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (ElasticCloudCcmAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/elastic-cloud/interfaces/elastic-cloud-ccm/accounts",
                "operation_id": "list_elastic_cloud_ccm_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_elastic_cloud_ccm_account_endpoint = _Endpoint(
            settings={
                "response_type": (ElasticCloudCcmAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/elastic-cloud/interfaces/elastic-cloud-ccm/accounts/{account_id}",
                "operation_id": "update_elastic_cloud_ccm_account",
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
                    "openapi_types": (ElasticCloudCcmAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_elastic_cloud_ccm_account(
        self,
        body: ElasticCloudCcmAccountRequest,
    ) -> ElasticCloudCcmAccountResponse:
        """Create an Elastic Cloud CCM account.

        Create an Elastic Cloud CCM (Cloud Cost Management) account.

        :type body: ElasticCloudCcmAccountRequest
        :rtype: ElasticCloudCcmAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_elastic_cloud_ccm_account_endpoint.call_with_http_info(**kwargs)

    def delete_elastic_cloud_ccm_account(
        self,
        account_id: str,
    ) -> None:
        """Delete an Elastic Cloud CCM account.

        Delete an Elastic Cloud CCM (Cloud Cost Management) account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_elastic_cloud_ccm_account_endpoint.call_with_http_info(**kwargs)

    def get_elastic_cloud_ccm_account(
        self,
        account_id: str,
    ) -> ElasticCloudCcmAccountResponse:
        """Get an Elastic Cloud CCM account.

        Get a single Elastic Cloud CCM (Cloud Cost Management) account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: ElasticCloudCcmAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_elastic_cloud_ccm_account_endpoint.call_with_http_info(**kwargs)

    def list_elastic_cloud_ccm_accounts(
        self,
    ) -> ElasticCloudCcmAccountsResponse:
        """List Elastic Cloud CCM accounts.

        List the Elastic Cloud CCM (Cloud Cost Management) accounts.

        :rtype: ElasticCloudCcmAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_elastic_cloud_ccm_accounts_endpoint.call_with_http_info(**kwargs)

    def update_elastic_cloud_ccm_account(
        self,
        account_id: str,
        body: ElasticCloudCcmAccountUpdateRequest,
    ) -> ElasticCloudCcmAccountResponse:
        """Update an Elastic Cloud CCM account.

        Update an Elastic Cloud CCM account. The update is a partial merge: only the fields provided are changed, so a name-only or settings-only update does not need to resend the full payload or write-only credentials.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: ElasticCloudCcmAccountUpdateRequest
        :rtype: ElasticCloudCcmAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_elastic_cloud_ccm_account_endpoint.call_with_http_info(**kwargs)
