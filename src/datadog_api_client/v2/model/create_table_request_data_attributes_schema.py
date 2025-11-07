# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_table_request_data_attributes_schema_fields_items import (
        CreateTableRequestDataAttributesSchemaFieldsItems,
    )


class CreateTableRequestDataAttributesSchema(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_table_request_data_attributes_schema_fields_items import (
            CreateTableRequestDataAttributesSchemaFieldsItems,
        )

        return {
            "fields": ([CreateTableRequestDataAttributesSchemaFieldsItems],),
            "primary_keys": ([str],),
        }

    attribute_map = {
        "fields": "fields",
        "primary_keys": "primary_keys",
    }

    def __init__(
        self_, fields: List[CreateTableRequestDataAttributesSchemaFieldsItems], primary_keys: List[str], **kwargs
    ):
        """
        Schema defining the structure and columns of the reference table.

        :param fields: The schema fields.
        :type fields: [CreateTableRequestDataAttributesSchemaFieldsItems]

        :param primary_keys: List of field names that serve as primary keys for the table. Only one primary key is supported, and it is used as an ID to retrieve rows.
        :type primary_keys: [str]
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.primary_keys = primary_keys
