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
    from datadog_api_client.v2.model.item_api_payload_data import ItemApiPayloadData
    from datadog_api_client.v2.model.item_api_payload_meta import ItemApiPayloadMeta


class ItemApiPayloadArray(ModelNormal):
    validations = {
        "data": {
            "max_items": 100,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.item_api_payload_data import ItemApiPayloadData
        from datadog_api_client.v2.model.item_api_payload_meta import ItemApiPayloadMeta

        return {
            "data": ([ItemApiPayloadData],),
            "meta": (ItemApiPayloadMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[ItemApiPayloadData], meta: Union[ItemApiPayloadMeta, UnsetType] = unset, **kwargs):
        """
        A collection of datastore items with pagination and schema metadata.

        :param data: An array of datastore items with their content and metadata.
        :type data: [ItemApiPayloadData]

        :param meta: Additional metadata about a collection of datastore items, including pagination and schema information.
        :type meta: ItemApiPayloadMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
