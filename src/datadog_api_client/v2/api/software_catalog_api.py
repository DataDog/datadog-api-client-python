# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.list_entity_catalog_response import ListEntityCatalogResponse
from datadog_api_client.v2.model.relation_type import RelationType
from datadog_api_client.v2.model.include_type import IncludeType
from datadog_api_client.v2.model.entity_data import EntityData
from datadog_api_client.v2.model.upsert_catalog_entity_response import UpsertCatalogEntityResponse
from datadog_api_client.v2.model.upsert_catalog_entity_request import UpsertCatalogEntityRequest
from datadog_api_client.v2.model.entity_v3 import EntityV3


class SoftwareCatalogApi:
    """
    API to create, update, retrieve, and delete Software Catalog entities.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._delete_catalog_entity_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/catalog/entity/{entity_id}",
                "operation_id": "delete_catalog_entity",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "entity_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "entity_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._list_catalog_entity_endpoint = _Endpoint(
            settings={
                "response_type": (ListEntityCatalogResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/catalog/entity",
                "operation_id": "list_catalog_entity",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "filter_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[id]",
                    "location": "query",
                },
                "filter_ref": {
                    "openapi_types": (str,),
                    "attribute": "filter[ref]",
                    "location": "query",
                },
                "filter_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[name]",
                    "location": "query",
                },
                "filter_kind": {
                    "openapi_types": (str,),
                    "attribute": "filter[kind]",
                    "location": "query",
                },
                "filter_owner": {
                    "openapi_types": (str,),
                    "attribute": "filter[owner]",
                    "location": "query",
                },
                "filter_relation_type": {
                    "openapi_types": (RelationType,),
                    "attribute": "filter[relation][type]",
                    "location": "query",
                },
                "filter_exclude_snapshot": {
                    "openapi_types": (str,),
                    "attribute": "filter[exclude_snapshot]",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (IncludeType,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._upsert_catalog_entity_endpoint = _Endpoint(
            settings={
                "response_type": (UpsertCatalogEntityResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/catalog/entity",
                "operation_id": "upsert_catalog_entity",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (UpsertCatalogEntityRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def delete_catalog_entity(
        self,
        entity_id: str,
    ) -> None:
        """Delete a single entity.

        Delete a single entity in Software Catalog.

        :param entity_id: UUID or Entity Ref.
        :type entity_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["entity_id"] = entity_id

        return self._delete_catalog_entity_endpoint.call_with_http_info(**kwargs)

    def list_catalog_entity(
        self,
        *,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        filter_id: Union[str, UnsetType] = unset,
        filter_ref: Union[str, UnsetType] = unset,
        filter_name: Union[str, UnsetType] = unset,
        filter_kind: Union[str, UnsetType] = unset,
        filter_owner: Union[str, UnsetType] = unset,
        filter_relation_type: Union[RelationType, UnsetType] = unset,
        filter_exclude_snapshot: Union[str, UnsetType] = unset,
        include: Union[IncludeType, UnsetType] = unset,
    ) -> ListEntityCatalogResponse:
        """Get a list of entities.

        Get a list of entities from Software Catalog.

        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param page_limit: Maximum number of entities in the response.
        :type page_limit: int, optional
        :param filter_id: Filter entities by UUID.
        :type filter_id: str, optional
        :param filter_ref: Filter entities by reference
        :type filter_ref: str, optional
        :param filter_name: Filter entities by name.
        :type filter_name: str, optional
        :param filter_kind: Filter entities by kind.
        :type filter_kind: str, optional
        :param filter_owner: Filter entities by owner.
        :type filter_owner: str, optional
        :param filter_relation_type: Filter entities by relation type.
        :type filter_relation_type: RelationType, optional
        :param filter_exclude_snapshot: Filter entities by excluding snapshotted entities.
        :type filter_exclude_snapshot: str, optional
        :param include: Include relationship data.
        :type include: IncludeType, optional
        :rtype: ListEntityCatalogResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if filter_id is not unset:
            kwargs["filter_id"] = filter_id

        if filter_ref is not unset:
            kwargs["filter_ref"] = filter_ref

        if filter_name is not unset:
            kwargs["filter_name"] = filter_name

        if filter_kind is not unset:
            kwargs["filter_kind"] = filter_kind

        if filter_owner is not unset:
            kwargs["filter_owner"] = filter_owner

        if filter_relation_type is not unset:
            kwargs["filter_relation_type"] = filter_relation_type

        if filter_exclude_snapshot is not unset:
            kwargs["filter_exclude_snapshot"] = filter_exclude_snapshot

        if include is not unset:
            kwargs["include"] = include

        return self._list_catalog_entity_endpoint.call_with_http_info(**kwargs)

    def list_catalog_entity_with_pagination(
        self,
        *,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        filter_id: Union[str, UnsetType] = unset,
        filter_ref: Union[str, UnsetType] = unset,
        filter_name: Union[str, UnsetType] = unset,
        filter_kind: Union[str, UnsetType] = unset,
        filter_owner: Union[str, UnsetType] = unset,
        filter_relation_type: Union[RelationType, UnsetType] = unset,
        filter_exclude_snapshot: Union[str, UnsetType] = unset,
        include: Union[IncludeType, UnsetType] = unset,
    ) -> collections.abc.Iterable[EntityData]:
        """Get a list of entities.

        Provide a paginated version of :meth:`list_catalog_entity`, returning all items.

        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param page_limit: Maximum number of entities in the response.
        :type page_limit: int, optional
        :param filter_id: Filter entities by UUID.
        :type filter_id: str, optional
        :param filter_ref: Filter entities by reference
        :type filter_ref: str, optional
        :param filter_name: Filter entities by name.
        :type filter_name: str, optional
        :param filter_kind: Filter entities by kind.
        :type filter_kind: str, optional
        :param filter_owner: Filter entities by owner.
        :type filter_owner: str, optional
        :param filter_relation_type: Filter entities by relation type.
        :type filter_relation_type: RelationType, optional
        :param filter_exclude_snapshot: Filter entities by excluding snapshotted entities.
        :type filter_exclude_snapshot: str, optional
        :param include: Include relationship data.
        :type include: IncludeType, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[EntityData]
        """
        kwargs: Dict[str, Any] = {}
        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if filter_id is not unset:
            kwargs["filter_id"] = filter_id

        if filter_ref is not unset:
            kwargs["filter_ref"] = filter_ref

        if filter_name is not unset:
            kwargs["filter_name"] = filter_name

        if filter_kind is not unset:
            kwargs["filter_kind"] = filter_kind

        if filter_owner is not unset:
            kwargs["filter_owner"] = filter_owner

        if filter_relation_type is not unset:
            kwargs["filter_relation_type"] = filter_relation_type

        if filter_exclude_snapshot is not unset:
            kwargs["filter_exclude_snapshot"] = filter_exclude_snapshot

        if include is not unset:
            kwargs["include"] = include

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 100)
        endpoint = self._list_catalog_entity_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def upsert_catalog_entity(
        self,
        body: Union[UpsertCatalogEntityRequest, EntityV3, str],
    ) -> UpsertCatalogEntityResponse:
        """Create or update entities.

        Create or update entities in Software Catalog.

        :param body: Entity YAML or JSON.
        :type body: UpsertCatalogEntityRequest
        :rtype: UpsertCatalogEntityResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._upsert_catalog_entity_endpoint.call_with_http_info(**kwargs)
