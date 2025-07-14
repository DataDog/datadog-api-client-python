# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.dataset_response_multi import DatasetResponseMulti
from datadog_api_client.v2.model.dataset_response_single import DatasetResponseSingle
from datadog_api_client.v2.model.dataset_create_request import DatasetCreateRequest


class DatasetsApi:
    """
    Data Access Controls in Datadog is a feature that allows administrators and access managers to regulate
    access to sensitive data. By defining Restricted Datasets, you can ensure that only specific teams or roles can
    view certain types of telemetry (for example, logs, traces, metrics, and RUM data).
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_dataset_endpoint = _Endpoint(
            settings={
                "response_type": (DatasetResponseSingle,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/datasets",
                "operation_id": "create_dataset",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DatasetCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_dataset_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/datasets/{dataset_id}",
                "operation_id": "delete_dataset",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_all_datasets_endpoint = _Endpoint(
            settings={
                "response_type": (DatasetResponseMulti,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/datasets",
                "operation_id": "get_all_datasets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_dataset_endpoint = _Endpoint(
            settings={
                "response_type": (DatasetResponseSingle,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/datasets/{dataset_id}",
                "operation_id": "get_dataset",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_dataset(
        self,
        body: DatasetCreateRequest,
    ) -> DatasetResponseSingle:
        """Create a dataset.

        Create a dataset with the configurations in the request.

        :param body: Dataset payload
        :type body: DatasetCreateRequest
        :rtype: DatasetResponseSingle
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_dataset_endpoint.call_with_http_info(**kwargs)

    def delete_dataset(
        self,
        dataset_id: str,
    ) -> None:
        """Delete a dataset.

        Deletes the dataset associated with the ID.

        :param dataset_id: The ID of a defined dataset.
        :type dataset_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dataset_id"] = dataset_id

        return self._delete_dataset_endpoint.call_with_http_info(**kwargs)

    def get_all_datasets(
        self,
    ) -> DatasetResponseMulti:
        """Get all datasets.

        Get all datasets that have been configured for an organization.

        :rtype: DatasetResponseMulti
        """
        kwargs: Dict[str, Any] = {}
        return self._get_all_datasets_endpoint.call_with_http_info(**kwargs)

    def get_dataset(
        self,
        dataset_id: str,
    ) -> DatasetResponseSingle:
        """Get a single dataset by ID.

        Retrieves the dataset associated with the ID.

        :param dataset_id: The ID of a defined dataset.
        :type dataset_id: str
        :rtype: DatasetResponseSingle
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dataset_id"] = dataset_id

        return self._get_dataset_endpoint.call_with_http_info(**kwargs)
