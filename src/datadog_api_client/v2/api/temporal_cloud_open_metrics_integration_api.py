# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_accounts_response import (
    TemporalCloudOpenMetricsIntegrationAccountsResponse,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_response import (
    TemporalCloudOpenMetricsIntegrationAccountResponse,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_create_request import (
    TemporalCloudOpenMetricsIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_update_request import (
    TemporalCloudOpenMetricsIntegrationAccountUpdateRequest,
)


class TemporalCloudOpenMetricsIntegrationApi:
    """
    Manage your Datadog Temporal Cloud OpenMetrics integration accounts and account resources
    directly through the Datadog API. See the
    `Temporal Cloud OpenMetrics integration page <https://docs.datadoghq.com/integrations/temporal-cloud-openmetrics/>`_ for
    more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_temporal_cloud_open_metrics_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (TemporalCloudOpenMetricsIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/temporal-cloud-openmetrics/accounts",
                "operation_id": "create_temporal_cloud_open_metrics_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TemporalCloudOpenMetricsIntegrationAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_temporal_cloud_open_metrics_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/temporal-cloud-openmetrics/accounts/{account_id}",
                "operation_id": "delete_temporal_cloud_open_metrics_integration_account",
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

        self._get_temporal_cloud_open_metrics_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (TemporalCloudOpenMetricsIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/temporal-cloud-openmetrics/accounts/{account_id}",
                "operation_id": "get_temporal_cloud_open_metrics_integration_account",
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

        self._list_temporal_cloud_open_metrics_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (TemporalCloudOpenMetricsIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/temporal-cloud-openmetrics/accounts",
                "operation_id": "list_temporal_cloud_open_metrics_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_temporal_cloud_open_metrics_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (TemporalCloudOpenMetricsIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/temporal-cloud-openmetrics/accounts/{account_id}",
                "operation_id": "update_temporal_cloud_open_metrics_integration_account",
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
                    "openapi_types": (TemporalCloudOpenMetricsIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_temporal_cloud_open_metrics_integration_account(
        self,
        body: TemporalCloudOpenMetricsIntegrationAccountCreateRequest,
    ) -> TemporalCloudOpenMetricsIntegrationAccountResponse:
        """Create a Temporal Cloud OpenMetrics account.

        Create a Temporal Cloud OpenMetrics integration account.

        :type body: TemporalCloudOpenMetricsIntegrationAccountCreateRequest
        :rtype: TemporalCloudOpenMetricsIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_temporal_cloud_open_metrics_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_temporal_cloud_open_metrics_integration_account(
        self,
        account_id: str,
    ) -> None:
        """Delete a Temporal Cloud OpenMetrics account.

        Delete a Temporal Cloud OpenMetrics integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_temporal_cloud_open_metrics_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_temporal_cloud_open_metrics_integration_account(
        self,
        account_id: str,
    ) -> TemporalCloudOpenMetricsIntegrationAccountResponse:
        """Get a Temporal Cloud OpenMetrics account.

        Get a Temporal Cloud OpenMetrics integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: TemporalCloudOpenMetricsIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_temporal_cloud_open_metrics_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_temporal_cloud_open_metrics_integration_accounts(
        self,
    ) -> TemporalCloudOpenMetricsIntegrationAccountsResponse:
        """List Temporal Cloud OpenMetrics accounts.

        List Temporal Cloud OpenMetrics integration accounts.

        :rtype: TemporalCloudOpenMetricsIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_temporal_cloud_open_metrics_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_temporal_cloud_open_metrics_integration_account(
        self,
        account_id: str,
        body: TemporalCloudOpenMetricsIntegrationAccountUpdateRequest,
    ) -> TemporalCloudOpenMetricsIntegrationAccountResponse:
        """Update a Temporal Cloud OpenMetrics account.

        Update a Temporal Cloud OpenMetrics integration account. Only the fields provided are changed.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: TemporalCloudOpenMetricsIntegrationAccountUpdateRequest
        :rtype: TemporalCloudOpenMetricsIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_temporal_cloud_open_metrics_integration_account_endpoint.call_with_http_info(**kwargs)
