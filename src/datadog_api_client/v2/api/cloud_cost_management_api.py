# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.aws_cur_configs_response import AwsCURConfigsResponse
from datadog_api_client.v2.model.aws_cur_config_response import AwsCURConfigResponse
from datadog_api_client.v2.model.aws_cur_config_post_request import AwsCURConfigPostRequest
from datadog_api_client.v2.model.aws_cur_config_patch_request import AwsCURConfigPatchRequest
from datadog_api_client.v2.model.aws_related_accounts_response import AWSRelatedAccountsResponse
from datadog_api_client.v2.model.azure_uc_configs_response import AzureUCConfigsResponse
from datadog_api_client.v2.model.azure_uc_config_pairs_response import AzureUCConfigPairsResponse
from datadog_api_client.v2.model.azure_uc_config_post_request import AzureUCConfigPostRequest
from datadog_api_client.v2.model.azure_uc_config_patch_request import AzureUCConfigPatchRequest
from datadog_api_client.v2.model.cloud_cost_activity_response import CloudCostActivityResponse


class CloudCostManagementApi:
    """
    The Cloud Cost Management API allows you to set up, edit, and delete Cloud Cost Management accounts for AWS and Azure. See the `Cloud Cost Management page <https://docs.datadoghq.com/cloud_cost_management/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_cost_awscur_config_endpoint = _Endpoint(
            settings={
                "response_type": (AwsCURConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/aws_cur_config",
                "operation_id": "create_cost_awscur_config",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AwsCURConfigPostRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_cost_azure_uc_configs_endpoint = _Endpoint(
            settings={
                "response_type": (AzureUCConfigPairsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/azure_uc_config",
                "operation_id": "create_cost_azure_uc_configs",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AzureUCConfigPostRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_cost_awscur_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/aws_cur_config/{cloud_account_id}",
                "operation_id": "delete_cost_awscur_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_cost_azure_uc_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/azure_uc_config/{cloud_account_id}",
                "operation_id": "delete_cost_azure_uc_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_cloud_cost_activity_endpoint = _Endpoint(
            settings={
                "response_type": (CloudCostActivityResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/enabled",
                "operation_id": "get_cloud_cost_activity",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_aws_related_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (AWSRelatedAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/aws_related_accounts",
                "operation_id": "list_aws_related_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_management_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "filter[management_account_id]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_cost_awscur_configs_endpoint = _Endpoint(
            settings={
                "response_type": (AwsCURConfigsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/aws_cur_config",
                "operation_id": "list_cost_awscur_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_cost_azure_uc_configs_endpoint = _Endpoint(
            settings={
                "response_type": (AzureUCConfigsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/azure_uc_config",
                "operation_id": "list_cost_azure_uc_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_cost_awscur_config_endpoint = _Endpoint(
            settings={
                "response_type": (AwsCURConfigsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/aws_cur_config/{cloud_account_id}",
                "operation_id": "update_cost_awscur_config",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AwsCURConfigPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_cost_azure_uc_configs_endpoint = _Endpoint(
            settings={
                "response_type": (AzureUCConfigPairsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/azure_uc_config/{cloud_account_id}",
                "operation_id": "update_cost_azure_uc_configs",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AzureUCConfigPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_cost_awscur_config(
        self,
        body: AwsCURConfigPostRequest,
    ) -> AwsCURConfigResponse:
        """Create Cloud Cost Management AWS CUR config.

        Create a Cloud Cost Management account for an AWS CUR config.

        :type body: AwsCURConfigPostRequest
        :rtype: AwsCURConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_cost_awscur_config_endpoint.call_with_http_info(**kwargs)

    def create_cost_azure_uc_configs(
        self,
        body: AzureUCConfigPostRequest,
    ) -> AzureUCConfigPairsResponse:
        """Create Cloud Cost Management Azure configs.

        Create a Cloud Cost Management account for an Azure config.

        :type body: AzureUCConfigPostRequest
        :rtype: AzureUCConfigPairsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_cost_azure_uc_configs_endpoint.call_with_http_info(**kwargs)

    def delete_cost_awscur_config(
        self,
        cloud_account_id: str,
    ) -> None:
        """Delete Cloud Cost Management AWS CUR config.

        Archive a Cloud Cost Management Account.

        :param cloud_account_id: Cloud Account id.
        :type cloud_account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        return self._delete_cost_awscur_config_endpoint.call_with_http_info(**kwargs)

    def delete_cost_azure_uc_config(
        self,
        cloud_account_id: str,
    ) -> None:
        """Delete Cloud Cost Management Azure config.

        Archive a Cloud Cost Management Account.

        :param cloud_account_id: Cloud Account id.
        :type cloud_account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        return self._delete_cost_azure_uc_config_endpoint.call_with_http_info(**kwargs)

    def get_cloud_cost_activity(
        self,
    ) -> CloudCostActivityResponse:
        """Cloud Cost Enabled.

        Get the Cloud Cost Management activity.

        :rtype: CloudCostActivityResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_cloud_cost_activity_endpoint.call_with_http_info(**kwargs)

    def list_aws_related_accounts(
        self,
        filter_management_account_id: str,
    ) -> AWSRelatedAccountsResponse:
        """List related AWS accounts.

        List the AWS accounts in an organization by calling 'organizations:ListAccounts' from the specified management account.

        :param filter_management_account_id: The ID of the management account to filter by.
        :type filter_management_account_id: str
        :rtype: AWSRelatedAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["filter_management_account_id"] = filter_management_account_id

        return self._list_aws_related_accounts_endpoint.call_with_http_info(**kwargs)

    def list_cost_awscur_configs(
        self,
    ) -> AwsCURConfigsResponse:
        """List Cloud Cost Management AWS CUR configs.

        List the AWS CUR configs.

        :rtype: AwsCURConfigsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_cost_awscur_configs_endpoint.call_with_http_info(**kwargs)

    def list_cost_azure_uc_configs(
        self,
    ) -> AzureUCConfigsResponse:
        """List Cloud Cost Management Azure configs.

        List the Azure configs.

        :rtype: AzureUCConfigsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_cost_azure_uc_configs_endpoint.call_with_http_info(**kwargs)

    def update_cost_awscur_config(
        self,
        cloud_account_id: str,
        body: AwsCURConfigPatchRequest,
    ) -> AwsCURConfigsResponse:
        """Update Cloud Cost Management AWS CUR config.

        Update the status of an AWS CUR config (active/archived).

        :param cloud_account_id: Cloud Account id.
        :type cloud_account_id: str
        :type body: AwsCURConfigPatchRequest
        :rtype: AwsCURConfigsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        kwargs["body"] = body

        return self._update_cost_awscur_config_endpoint.call_with_http_info(**kwargs)

    def update_cost_azure_uc_configs(
        self,
        cloud_account_id: str,
        body: AzureUCConfigPatchRequest,
    ) -> AzureUCConfigPairsResponse:
        """Update Cloud Cost Management Azure config.

        Update the status of an  Azure config (active/archived).

        :param cloud_account_id: Cloud Account id.
        :type cloud_account_id: str
        :type body: AzureUCConfigPatchRequest
        :rtype: AzureUCConfigPairsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        kwargs["body"] = body

        return self._update_cost_azure_uc_configs_endpoint.call_with_http_info(**kwargs)
