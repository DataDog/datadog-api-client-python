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
    from datadog_api_client.v2.model.item_api_payload_meta_schema_field import ItemApiPayloadMetaSchemaField


class ItemApiPayloadMetaSchema(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.item_api_payload_meta_schema_field import ItemApiPayloadMetaSchemaField

        return {
            "fields": ([ItemApiPayloadMetaSchemaField],),
            "primary_key": (str,),
        }

    attribute_map = {
        "fields": "fields",
        "primary_key": "primary_key",
    }

    def __init__(
        self_,
        fields: Union[List[ItemApiPayloadMetaSchemaField], UnsetType] = unset,
        primary_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema information about the datastore, including its primary key and field definitions.

        :param fields: An array describing the columns available in this datastore.
        :type fields: [ItemApiPayloadMetaSchemaField], optional

        :param primary_key: The name of the primary key column for this datastore.
        :type primary_key: str, optional
        """
        if fields is not unset:
            kwargs["fields"] = fields
        if primary_key is not unset:
            kwargs["primary_key"] = primary_key
        super().__init__(kwargs)
