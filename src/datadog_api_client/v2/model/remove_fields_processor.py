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
    from datadog_api_client.v2.model.remove_fields_processor_type import RemoveFieldsProcessorType


class RemoveFieldsProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remove_fields_processor_type import RemoveFieldsProcessorType

        return {
            "fields": ([str],),
            "id": (str,),
            "inputs": ([str],),
            "type": (RemoveFieldsProcessorType,),
        }

    attribute_map = {
        "fields": "fields",
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(self_, fields: List[str], id: str, inputs: List[str], type: RemoveFieldsProcessorType, **kwargs):
        """
        The ``remove_fields`` processor deletes specified fields from logs.

        :param fields: The ``RemoveFieldsProcessor`` ``fields``.
        :type fields: [str]

        :param id: The ``RemoveFieldsProcessor`` ``id``.
        :type id: str

        :param inputs: The ``RemoveFieldsProcessor`` ``inputs``.
        :type inputs: [str]

        :param type: The definition of ``RemoveFieldsProcessorType`` object.
        :type type: RemoveFieldsProcessorType
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.id = id
        self_.inputs = inputs
        self_.type = type
