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
from datadog_api_client.v2.model.datastore_array import DatastoreArray
from datadog_api_client.v2.model.create_apps_datastore_response import CreateAppsDatastoreResponse
from datadog_api_client.v2.model.create_apps_datastore_request import CreateAppsDatastoreRequest
from datadog_api_client.v2.model.datastore import Datastore
from datadog_api_client.v2.model.update_apps_datastore_request import UpdateAppsDatastoreRequest
from datadog_api_client.v2.model.delete_apps_datastore_item_response import DeleteAppsDatastoreItemResponse
from datadog_api_client.v2.model.delete_apps_datastore_item_request import DeleteAppsDatastoreItemRequest
from datadog_api_client.v2.model.item_api_payload_array import ItemApiPayloadArray
from datadog_api_client.v2.model.item_api_payload import ItemApiPayload
from datadog_api_client.v2.model.update_apps_datastore_item_request import UpdateAppsDatastoreItemRequest
from datadog_api_client.v2.model.delete_apps_datastore_item_response_array import DeleteAppsDatastoreItemResponseArray
from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request import BulkDeleteAppsDatastoreItemsRequest
from datadog_api_client.v2.model.put_apps_datastore_item_response_array import PutAppsDatastoreItemResponseArray
from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request import BulkPutAppsDatastoreItemsRequest


class ActionsDatastoresApi:
    """
    Leverage the Actions Datastore API to create, modify, and delete
    items in datastores owned by your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._bulk_delete_datastore_items_endpoint = _Endpoint(
            settings={
                "response_type": (DeleteAppsDatastoreItemResponseArray,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions-datastores/{datastore_id}/items/bulk",
                "operation_id": "bulk_delete_datastore_items",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "datastore_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "datastore_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (BulkDeleteAppsDatastoreItemsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._bulk_write_datastore_items_endpoint = _Endpoint(
            settings={
                "response_type": (PutAppsDatastoreItemResponseArray,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions-datastores/{datastore_id}/items/bulk",
                "operation_id": "bulk_write_datastore_items",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "datastore_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "datastore_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (BulkPutAppsDatastoreItemsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_datastore_endpoint = _Endpoint(
            settings={
                "response_type": (CreateAppsDatastoreResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions-datastores",
                "operation_id": "create_datastore",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateAppsDatastoreRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_datastore_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions-datastores/{datastore_id}",
                "operation_id": "delete_datastore",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "datastore_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "datastore_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_datastore_item_endpoint = _Endpoint(
            settings={
                "response_type": (DeleteAppsDatastoreItemResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions-datastores/{datastore_id}/items",
                "operation_id": "delete_datastore_item",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "datastore_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "datastore_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DeleteAppsDatastoreItemRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_datastore_endpoint = _Endpoint(
            settings={
                "response_type": (Datastore,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions-datastores/{datastore_id}",
                "operation_id": "get_datastore",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "datastore_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "datastore_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_datastore_items_endpoint = _Endpoint(
            settings={
                "response_type": (ItemApiPayloadArray,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions-datastores/{datastore_id}/items",
                "operation_id": "list_datastore_items",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "datastore_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "datastore_id",
                    "location": "path",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "item_key": {
                    "validation": {
                        "max_length": 256,
                    },
                    "openapi_types": (str,),
                    "attribute": "item_key",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_datastores_endpoint = _Endpoint(
            settings={
                "response_type": (DatastoreArray,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions-datastores",
                "operation_id": "list_datastores",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_datastore_endpoint = _Endpoint(
            settings={
                "response_type": (Datastore,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions-datastores/{datastore_id}",
                "operation_id": "update_datastore",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "datastore_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "datastore_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateAppsDatastoreRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_datastore_item_endpoint = _Endpoint(
            settings={
                "response_type": (ItemApiPayload,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions-datastores/{datastore_id}/items",
                "operation_id": "update_datastore_item",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "datastore_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "datastore_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateAppsDatastoreItemRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def bulk_delete_datastore_items(
        self,
        datastore_id: str,
        body: BulkDeleteAppsDatastoreItemsRequest,
    ) -> DeleteAppsDatastoreItemResponseArray:
        """Bulk delete datastore items.

        Deletes multiple items from a datastore by their keys in a single operation.

        :param datastore_id: The ID of the datastore.
        :type datastore_id: str
        :type body: BulkDeleteAppsDatastoreItemsRequest
        :rtype: DeleteAppsDatastoreItemResponseArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["datastore_id"] = datastore_id

        kwargs["body"] = body

        return self._bulk_delete_datastore_items_endpoint.call_with_http_info(**kwargs)

    def bulk_write_datastore_items(
        self,
        datastore_id: str,
        body: BulkPutAppsDatastoreItemsRequest,
    ) -> PutAppsDatastoreItemResponseArray:
        """Bulk write datastore items.

        Creates or replaces multiple items in a datastore by their keys in a single operation.

        :param datastore_id: The unique identifier of the datastore to retrieve.
        :type datastore_id: str
        :type body: BulkPutAppsDatastoreItemsRequest
        :rtype: PutAppsDatastoreItemResponseArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["datastore_id"] = datastore_id

        kwargs["body"] = body

        return self._bulk_write_datastore_items_endpoint.call_with_http_info(**kwargs)

    def create_datastore(
        self,
        body: CreateAppsDatastoreRequest,
    ) -> CreateAppsDatastoreResponse:
        """Create datastore.

        Creates a new datastore.

        :type body: CreateAppsDatastoreRequest
        :rtype: CreateAppsDatastoreResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_datastore_endpoint.call_with_http_info(**kwargs)

    def delete_datastore(
        self,
        datastore_id: str,
    ) -> None:
        """Delete datastore.

        Deletes a datastore by its unique identifier.

        :param datastore_id: The unique identifier of the datastore to retrieve.
        :type datastore_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["datastore_id"] = datastore_id

        return self._delete_datastore_endpoint.call_with_http_info(**kwargs)

    def delete_datastore_item(
        self,
        datastore_id: str,
        body: DeleteAppsDatastoreItemRequest,
    ) -> DeleteAppsDatastoreItemResponse:
        """Delete datastore item.

        Deletes an item from a datastore by its key.

        :param datastore_id: The unique identifier of the datastore to retrieve.
        :type datastore_id: str
        :type body: DeleteAppsDatastoreItemRequest
        :rtype: DeleteAppsDatastoreItemResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["datastore_id"] = datastore_id

        kwargs["body"] = body

        return self._delete_datastore_item_endpoint.call_with_http_info(**kwargs)

    def get_datastore(
        self,
        datastore_id: str,
    ) -> Datastore:
        """Get datastore.

        Retrieves a specific datastore by its ID.

        :param datastore_id: The unique identifier of the datastore to retrieve.
        :type datastore_id: str
        :rtype: Datastore
        """
        kwargs: Dict[str, Any] = {}
        kwargs["datastore_id"] = datastore_id

        return self._get_datastore_endpoint.call_with_http_info(**kwargs)

    def list_datastore_items(
        self,
        datastore_id: str,
        *,
        filter: Union[str, UnsetType] = unset,
        item_key: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
    ) -> ItemApiPayloadArray:
        """List datastore items.

        Lists items from a datastore. You can filter the results by specifying either an item key or a filter query parameter, but not both at the same time. Supports server-side pagination for large datasets.

        :param datastore_id: The unique identifier of the datastore to retrieve.
        :type datastore_id: str
        :param filter: Optional query filter to search items using the `logs search syntax <https://docs.datadoghq.com/logs/explorer/search_syntax/>`_.
        :type filter: str, optional
        :param item_key: Optional primary key value to retrieve a specific item. Cannot be used together with the filter parameter.
        :type item_key: str, optional
        :param page_limit: Optional field to limit the number of items to return per page for pagination. Up to 100 items can be returned per page.
        :type page_limit: int, optional
        :param page_offset: Optional field to offset the number of items to skip from the beginning of the result set for pagination.
        :type page_offset: int, optional
        :param sort: Optional field to sort results by. Prefix with '-' for descending order (e.g., '-created_at').
        :type sort: str, optional
        :rtype: ItemApiPayloadArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["datastore_id"] = datastore_id

        if filter is not unset:
            kwargs["filter"] = filter

        if item_key is not unset:
            kwargs["item_key"] = item_key

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_datastore_items_endpoint.call_with_http_info(**kwargs)

    def list_datastores(
        self,
    ) -> DatastoreArray:
        """List datastores.

        Lists all datastores for the organization.

        :rtype: DatastoreArray
        """
        kwargs: Dict[str, Any] = {}
        return self._list_datastores_endpoint.call_with_http_info(**kwargs)

    def update_datastore(
        self,
        datastore_id: str,
        body: UpdateAppsDatastoreRequest,
    ) -> Datastore:
        """Update datastore.

        Updates an existing datastore's attributes.

        :param datastore_id: The unique identifier of the datastore to retrieve.
        :type datastore_id: str
        :type body: UpdateAppsDatastoreRequest
        :rtype: Datastore
        """
        kwargs: Dict[str, Any] = {}
        kwargs["datastore_id"] = datastore_id

        kwargs["body"] = body

        return self._update_datastore_endpoint.call_with_http_info(**kwargs)

    def update_datastore_item(
        self,
        datastore_id: str,
        body: UpdateAppsDatastoreItemRequest,
    ) -> ItemApiPayload:
        """Update datastore item.

        Partially updates an item in a datastore by its key.

        :param datastore_id: The unique identifier of the datastore to retrieve.
        :type datastore_id: str
        :type body: UpdateAppsDatastoreItemRequest
        :rtype: ItemApiPayload
        """
        kwargs: Dict[str, Any] = {}
        kwargs["datastore_id"] = datastore_id

        kwargs["body"] = body

        return self._update_datastore_item_endpoint.call_with_http_info(**kwargs)
