# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relation_response import RelationResponse
    from datadog_api_client.v2.model.entity_data import EntityData
    from datadog_api_client.v2.model.list_relation_catalog_response_links import ListRelationCatalogResponseLinks
    from datadog_api_client.v2.model.relation_response_meta import RelationResponseMeta


class ListRelationCatalogResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relation_response import RelationResponse
        from datadog_api_client.v2.model.entity_data import EntityData
        from datadog_api_client.v2.model.list_relation_catalog_response_links import ListRelationCatalogResponseLinks
        from datadog_api_client.v2.model.relation_response_meta import RelationResponseMeta

        return {
            "data": ([RelationResponse],),
            "included": ([EntityData],),
            "links": (ListRelationCatalogResponseLinks,),
            "meta": (RelationResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[RelationResponse], UnsetType] = unset,
        included: Union[List[EntityData], UnsetType] = unset,
        links: Union[ListRelationCatalogResponseLinks, UnsetType] = unset,
        meta: Union[RelationResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        List entity relation response.

        :param data: Array of relation responses
        :type data: [RelationResponse], optional

        :param included: List relation response included entities.
        :type included: [EntityData], optional

        :param links: List relation response links.
        :type links: ListRelationCatalogResponseLinks, optional

        :param meta: Relation response metadata.
        :type meta: RelationResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
