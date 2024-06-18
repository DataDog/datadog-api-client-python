# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    file_type,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.org_config_list_response import OrgConfigListResponse
from datadog_api_client.v2.model.org_config_get_response import OrgConfigGetResponse
from datadog_api_client.v2.model.org_config_write_request import OrgConfigWriteRequest


class OrganizationsApi:
    """
    Create, edit, and manage your organizations. Read more about `multi-org accounts <https://docs.datadoghq.com/account_management/multi_organization>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_org_config_endpoint = _Endpoint(
            settings={
                "response_type": (OrgConfigGetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_configs/{org_config_name}",
                "operation_id": "get_org_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "org_config_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "org_config_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_org_configs_endpoint = _Endpoint(
            settings={
                "response_type": (OrgConfigListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_configs",
                "operation_id": "list_org_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_org_config_endpoint = _Endpoint(
            settings={
                "response_type": (OrgConfigGetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_configs/{org_config_name}",
                "operation_id": "update_org_config",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "org_config_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "org_config_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OrgConfigWriteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upload_idp_metadata_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/saml_configurations/idp_metadata",
                "operation_id": "upload_idp_metadata",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "idp_file": {
                    "openapi_types": (file_type,),
                    "attribute": "idp_file",
                    "location": "form",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["multipart/form-data"]},
            api_client=api_client,
        )

    def get_org_config(
        self,
        org_config_name: str,
    ) -> OrgConfigGetResponse:
        """Get a specific Org Config value.

        Return the name, description, and value of a specific Org Config.

        :param org_config_name: The name of an Org Config.
        :type org_config_name: str
        :rtype: OrgConfigGetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_config_name"] = org_config_name

        return self._get_org_config_endpoint.call_with_http_info(**kwargs)

    def list_org_configs(
        self,
    ) -> OrgConfigListResponse:
        """List Org Configs.

        Returns all Org Configs (name, description, and value).

        :rtype: OrgConfigListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_org_configs_endpoint.call_with_http_info(**kwargs)

    def update_org_config(
        self,
        org_config_name: str,
        body: OrgConfigWriteRequest,
    ) -> OrgConfigGetResponse:
        """Update a specific Org Config.

        Update the value of a specific Org Config.

        :param org_config_name: The name of an Org Config.
        :type org_config_name: str
        :type body: OrgConfigWriteRequest
        :rtype: OrgConfigGetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_config_name"] = org_config_name

        kwargs["body"] = body

        return self._update_org_config_endpoint.call_with_http_info(**kwargs)

    def upload_idp_metadata(
        self,
        *,
        idp_file: Union[file_type, UnsetType] = unset,
    ) -> None:
        """Upload IdP metadata.

        Endpoint for uploading IdP metadata for SAML setup.

        Use this endpoint to upload or replace IdP metadata for SAML login configuration.

        :param idp_file: The IdP metadata XML file
        :type idp_file: file_type, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        if idp_file is not unset:
            kwargs["idp_file"] = idp_file

        return self._upload_idp_metadata_endpoint.call_with_http_info(**kwargs)
