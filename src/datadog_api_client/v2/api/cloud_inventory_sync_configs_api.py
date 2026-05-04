# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.cloud_inventory_sync_config_response import CloudInventorySyncConfigResponse
from datadog_api_client.v2.model.upsert_cloud_inventory_sync_config_request import UpsertCloudInventorySyncConfigRequest


class CloudInventorySyncConfigsApi:
    """
    Configure cloud inventory file synchronization from your cloud storage to Datadog.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._upsert_sync_config_endpoint = _Endpoint(
            settings={
                "response_type": (CloudInventorySyncConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cloudinventoryservice/syncconfigs",
                "operation_id": "upsert_sync_config",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (UpsertCloudInventorySyncConfigRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def upsert_sync_config(
        self,
        body: UpsertCloudInventorySyncConfigRequest,
    ) -> CloudInventorySyncConfigResponse:
        """Create or update a sync configuration.

        Create or update a cloud inventory sync configuration. Specify the cloud provider in ``data.id``
        and provider-specific settings under ``data.attributes``. This endpoint uses an upsert model.

        :type body: UpsertCloudInventorySyncConfigRequest
        :rtype: CloudInventorySyncConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._upsert_sync_config_endpoint.call_with_http_info(**kwargs)
