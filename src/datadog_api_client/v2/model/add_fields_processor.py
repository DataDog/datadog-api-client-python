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
    from datadog_api_client.v2.model.field_item import FieldItem
    from datadog_api_client.v2.model.add_fields_processor_type import AddFieldsProcessorType


class AddFieldsProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.field_item import FieldItem
        from datadog_api_client.v2.model.add_fields_processor_type import AddFieldsProcessorType

        return {
            "fields": ([FieldItem],),
            "id": (str,),
            "inputs": ([str],),
            "type": (AddFieldsProcessorType,),
        }

    attribute_map = {
        "fields": "fields",
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(self_, fields: List[FieldItem], id: str, inputs: List[str], type: AddFieldsProcessorType, **kwargs):
        """
        The ``add_fields`` processor adds static key-value fields to logs.

        :param fields: The ``AddFieldsProcessor`` ``fields``.
        :type fields: [FieldItem]

        :param id: The ``AddFieldsProcessor`` ``id``.
        :type id: str

        :param inputs: The ``AddFieldsProcessor`` ``inputs``.
        :type inputs: [str]

        :param type: The definition of ``AddFieldsProcessorType`` object.
        :type type: AddFieldsProcessorType
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.id = id
        self_.inputs = inputs
        self_.type = type
