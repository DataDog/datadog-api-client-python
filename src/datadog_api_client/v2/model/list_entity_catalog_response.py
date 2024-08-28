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
    from datadog_api_client.v2.model.entity_data import EntityData
    from datadog_api_client.v2.model.list_entity_catalog_response_included_item import (
        ListEntityCatalogResponseIncludedItem,
    )
    from datadog_api_client.v2.model.list_entity_catalog_response_links import ListEntityCatalogResponseLinks
    from datadog_api_client.v2.model.entity_response_meta import EntityResponseMeta
    from datadog_api_client.v2.model.entity_response_included_schema import EntityResponseIncludedSchema
    from datadog_api_client.v2.model.entity_response_included_raw_schema import EntityResponseIncludedRawSchema
    from datadog_api_client.v2.model.entity_response_included_related_entity import EntityResponseIncludedRelatedEntity
    from datadog_api_client.v2.model.entity_response_included_oncall import EntityResponseIncludedOncall
    from datadog_api_client.v2.model.entity_response_included_incident import EntityResponseIncludedIncident


class ListEntityCatalogResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_data import EntityData
        from datadog_api_client.v2.model.list_entity_catalog_response_included_item import (
            ListEntityCatalogResponseIncludedItem,
        )
        from datadog_api_client.v2.model.list_entity_catalog_response_links import ListEntityCatalogResponseLinks
        from datadog_api_client.v2.model.entity_response_meta import EntityResponseMeta

        return {
            "data": ([EntityData],),
            "included": ([ListEntityCatalogResponseIncludedItem],),
            "links": (ListEntityCatalogResponseLinks,),
            "meta": (EntityResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[EntityData], UnsetType] = unset,
        included: Union[
            List[
                Union[
                    ListEntityCatalogResponseIncludedItem,
                    EntityResponseIncludedSchema,
                    EntityResponseIncludedRawSchema,
                    EntityResponseIncludedRelatedEntity,
                    EntityResponseIncludedOncall,
                    EntityResponseIncludedIncident,
                ]
            ],
            UnsetType,
        ] = unset,
        links: Union[ListEntityCatalogResponseLinks, UnsetType] = unset,
        meta: Union[EntityResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        List entity response.

        :param data: List of entity data.
        :type data: [EntityData], optional

        :param included: List entity response included.
        :type included: [ListEntityCatalogResponseIncludedItem], optional

        :param links: List entity response links.
        :type links: ListEntityCatalogResponseLinks, optional

        :param meta: Entity metadata.
        :type meta: EntityResponseMeta, optional
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
