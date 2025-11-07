# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.reference_table_schema_field_type import ReferenceTableSchemaFieldType


class PatchTableRequestDataAttributesSchemaFieldsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.reference_table_schema_field_type import ReferenceTableSchemaFieldType

        return {
            "name": (str,),
            "type": (ReferenceTableSchemaFieldType,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self_, name: str, type: ReferenceTableSchemaFieldType, **kwargs):
        """
        A single field (column) in the reference table schema to be updated. Schema fields cannot be deleted or renamed.

        :param name: The field name.
        :type name: str

        :param type: The field type for reference table schema fields.
        :type type: ReferenceTableSchemaFieldType
        """
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
