# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.table_result_v2_array import TableResultV2Array
from datadog_api_client.v2.model.reference_table_sort_type import ReferenceTableSortType
from datadog_api_client.v2.model.table_result_v2 import TableResultV2
from datadog_api_client.v2.model.create_table_request import CreateTableRequest
from datadog_api_client.v2.model.patch_table_request import PatchTableRequest
from datadog_api_client.v2.model.batch_delete_rows_request_array import BatchDeleteRowsRequestArray
from datadog_api_client.v2.model.table_row_resource_array import TableRowResourceArray
from datadog_api_client.v2.model.batch_upsert_rows_request_array import BatchUpsertRowsRequestArray
from datadog_api_client.v2.model.create_upload_response import CreateUploadResponse
from datadog_api_client.v2.model.create_upload_request import CreateUploadRequest


class ReferenceTablesApi:
    """
    View and manage Reference Tables in your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_reference_table_endpoint = _Endpoint(
            settings={
                "response_type": (TableResultV2,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/reference-tables/tables",
                "operation_id": "create_reference_table",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateTableRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_reference_table_upload_endpoint = _Endpoint(
            settings={
                "response_type": (CreateUploadResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/reference-tables/uploads",
                "operation_id": "create_reference_table_upload",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateUploadRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_rows_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/reference-tables/tables/{id}/rows",
                "operation_id": "delete_rows",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (BatchDeleteRowsRequestArray,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_table_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/reference-tables/tables/{id}",
                "operation_id": "delete_table",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_rows_by_id_endpoint = _Endpoint(
            settings={
                "response_type": (TableRowResourceArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/reference-tables/tables/{id}/rows",
                "operation_id": "get_rows_by_id",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "row_id": {
                    "required": True,
                    "openapi_types": ([str],),
                    "attribute": "row_id",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_table_endpoint = _Endpoint(
            settings={
                "response_type": (TableResultV2,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/reference-tables/tables/{id}",
                "operation_id": "get_table",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_tables_endpoint = _Endpoint(
            settings={
                "response_type": (TableResultV2Array,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/reference-tables/tables",
                "operation_id": "list_tables",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
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
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (ReferenceTableSortType,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter_status": {
                    "openapi_types": (str,),
                    "attribute": "filter[status]",
                    "location": "query",
                },
                "filter_table_name_exact": {
                    "openapi_types": (str,),
                    "attribute": "filter[table_name][exact]",
                    "location": "query",
                },
                "filter_table_name_contains": {
                    "openapi_types": (str,),
                    "attribute": "filter[table_name][contains]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_reference_table_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/reference-tables/tables/{id}",
                "operation_id": "update_reference_table",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PatchTableRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upsert_rows_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/reference-tables/tables/{id}/rows",
                "operation_id": "upsert_rows",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (BatchUpsertRowsRequestArray,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_reference_table(
        self,
        body: CreateTableRequest,
    ) -> TableResultV2:
        """Create reference table.

        Creates a reference table. You can provide data in two ways:

        #. Call POST /api/v2/reference-tables/upload to get an upload ID. Then, PUT the CSV data
           (not the file itself) in chunks to each URL in the request body. Finally, call this
           POST endpoint with ``upload_id`` in ``file_metadata``.
        #. Provide ``access_details`` in ``file_metadata`` pointing to a CSV file in cloud storage.

        :type body: CreateTableRequest
        :rtype: TableResultV2
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_reference_table_endpoint.call_with_http_info(**kwargs)

    def create_reference_table_upload(
        self,
        body: CreateUploadRequest,
    ) -> CreateUploadResponse:
        """Create reference table upload.

        Create a reference table upload for bulk data ingestion

        :type body: CreateUploadRequest
        :rtype: CreateUploadResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_reference_table_upload_endpoint.call_with_http_info(**kwargs)

    def delete_rows(
        self,
        id: str,
        body: BatchDeleteRowsRequestArray,
    ) -> None:
        """Delete rows.

        Delete multiple rows from a Reference Table by their primary key values.

        :param id: Unique identifier of the reference table to delete rows from
        :type id: str
        :type body: BatchDeleteRowsRequestArray
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._delete_rows_endpoint.call_with_http_info(**kwargs)

    def delete_table(
        self,
        id: str,
    ) -> None:
        """Delete table.

        Delete a reference table by ID

        :param id: Unique identifier of the reference table to delete
        :type id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_table_endpoint.call_with_http_info(**kwargs)

    def get_rows_by_id(
        self,
        id: str,
        row_id: List[str],
    ) -> TableRowResourceArray:
        """Get rows by id.

        Get reference table rows by their primary key values.

        :param id: Unique identifier of the reference table to get rows from
        :type id: str
        :param row_id: List of row IDs (primary key values) to retrieve from the reference table.
        :type row_id: [str]
        :rtype: TableRowResourceArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["row_id"] = row_id

        return self._get_rows_by_id_endpoint.call_with_http_info(**kwargs)

    def get_table(
        self,
        id: str,
    ) -> TableResultV2:
        """Get table.

        Get a reference table by ID

        :param id: Unique identifier of the reference table to retrieve
        :type id: str
        :rtype: TableResultV2
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_table_endpoint.call_with_http_info(**kwargs)

    def list_tables(
        self,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        sort: Union[ReferenceTableSortType, UnsetType] = unset,
        filter_status: Union[str, UnsetType] = unset,
        filter_table_name_exact: Union[str, UnsetType] = unset,
        filter_table_name_contains: Union[str, UnsetType] = unset,
    ) -> TableResultV2Array:
        """List tables.

        List all reference tables in this organization.

        :param page_limit: Number of tables to return.
        :type page_limit: int, optional
        :param page_offset: Number of tables to skip for pagination.
        :type page_offset: int, optional
        :param sort: Sort field and direction for the list of reference tables. Use field name for ascending, prefix with "-" for descending.
        :type sort: ReferenceTableSortType, optional
        :param filter_status: Filter by table status.
        :type filter_status: str, optional
        :param filter_table_name_exact: Filter by exact table name match.
        :type filter_table_name_exact: str, optional
        :param filter_table_name_contains: Filter by table name containing substring.
        :type filter_table_name_contains: str, optional
        :rtype: TableResultV2Array
        """
        kwargs: Dict[str, Any] = {}
        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if sort is not unset:
            kwargs["sort"] = sort

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        if filter_table_name_exact is not unset:
            kwargs["filter_table_name_exact"] = filter_table_name_exact

        if filter_table_name_contains is not unset:
            kwargs["filter_table_name_contains"] = filter_table_name_contains

        return self._list_tables_endpoint.call_with_http_info(**kwargs)

    def update_reference_table(
        self,
        id: str,
        body: PatchTableRequest,
    ) -> None:
        """Update reference table.

        Update a reference table by ID. You can update the table's data, description, and tags. Note: The source type cannot be changed after table creation. For data updates: For existing tables of type `source:LOCAL_FILE`, call POST api/v2/reference-tables/uploads first to get an upload ID, then PUT chunks of CSV data to each provided URL, and finally call this PATCH endpoint with the upload_id in file_metadata. For existing tables with `source:` types of `S3 ``,`` GCS ``, or`` AZURE`, provide updated access_details in file_metadata pointing to a CSV file in the same type of cloud storage.

        :param id: Unique identifier of the reference table to update
        :type id: str
        :type body: PatchTableRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_reference_table_endpoint.call_with_http_info(**kwargs)

    def upsert_rows(
        self,
        id: str,
        body: BatchUpsertRowsRequestArray,
    ) -> None:
        """Upsert rows.

        Create or update rows in a Reference Table by their primary key values. If a row with the specified primary key exists, it is updated; otherwise, a new row is created.

        :param id: Unique identifier of the reference table to upsert rows into
        :type id: str
        :type body: BatchUpsertRowsRequestArray
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._upsert_rows_endpoint.call_with_http_info(**kwargs)
