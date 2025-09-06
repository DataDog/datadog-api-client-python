# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.item_api_payload_meta_page import ItemApiPayloadMetaPage
    from datadog_api_client.v2.model.item_api_payload_meta_schema import ItemApiPayloadMetaSchema


class ItemApiPayloadMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.item_api_payload_meta_page import ItemApiPayloadMetaPage
        from datadog_api_client.v2.model.item_api_payload_meta_schema import ItemApiPayloadMetaSchema

        return {
            "page": (ItemApiPayloadMetaPage,),
            "schema": (ItemApiPayloadMetaSchema,),
        }

    attribute_map = {
        "page": "page",
        "schema": "schema",
    }

    def __init__(
        self_,
        page: Union[ItemApiPayloadMetaPage, UnsetType] = unset,
        schema: Union[ItemApiPayloadMetaSchema, UnsetType] = unset,
        **kwargs,
    ):
        """
        Additional metadata about a collection of datastore items, including pagination and schema information.

        :param page: Pagination information for a collection of datastore items.
        :type page: ItemApiPayloadMetaPage, optional

        :param schema: Schema information about the datastore, including its primary key and field definitions.
        :type schema: ItemApiPayloadMetaSchema, optional
        """
        if page is not unset:
            kwargs["page"] = page
        if schema is not unset:
            kwargs["schema"] = schema
        super().__init__(kwargs)
