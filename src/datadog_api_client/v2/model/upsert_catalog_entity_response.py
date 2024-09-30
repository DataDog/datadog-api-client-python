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
    from datadog_api_client.v2.model.upsert_catalog_entity_response_included_item import (
        UpsertCatalogEntityResponseIncludedItem,
    )
    from datadog_api_client.v2.model.entity_response_meta import EntityResponseMeta
    from datadog_api_client.v2.model.entity_response_included_schema import EntityResponseIncludedSchema


class UpsertCatalogEntityResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_data import EntityData
        from datadog_api_client.v2.model.upsert_catalog_entity_response_included_item import (
            UpsertCatalogEntityResponseIncludedItem,
        )
        from datadog_api_client.v2.model.entity_response_meta import EntityResponseMeta

        return {
            "data": ([EntityData],),
            "included": ([UpsertCatalogEntityResponseIncludedItem],),
            "meta": (EntityResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[EntityData], UnsetType] = unset,
        included: Union[
            List[Union[UpsertCatalogEntityResponseIncludedItem, EntityResponseIncludedSchema]], UnsetType
        ] = unset,
        meta: Union[EntityResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Upsert entity response.

        :param data: List of entity data.
        :type data: [EntityData], optional

        :param included: Upsert entity response included.
        :type included: [UpsertCatalogEntityResponseIncludedItem], optional

        :param meta: Entity metadata.
        :type meta: EntityResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
