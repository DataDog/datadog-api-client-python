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
    from datadog_api_client.v2.model.rename_fields_processor_fields_items import RenameFieldsProcessorFieldsItems
    from datadog_api_client.v2.model.rename_fields_processor_type import RenameFieldsProcessorType


class RenameFieldsProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rename_fields_processor_fields_items import RenameFieldsProcessorFieldsItems
        from datadog_api_client.v2.model.rename_fields_processor_type import RenameFieldsProcessorType

        return {
            "fields": ([RenameFieldsProcessorFieldsItems],),
            "id": (str,),
            "inputs": ([str],),
            "type": (RenameFieldsProcessorType,),
        }

    attribute_map = {
        "fields": "fields",
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        fields: List[RenameFieldsProcessorFieldsItems],
        id: str,
        inputs: List[str],
        type: RenameFieldsProcessorType,
        **kwargs,
    ):
        """
        The ``rename_fields`` processor changes field names.

        :param fields: The ``RenameFieldsProcessor`` ``fields``.
        :type fields: [RenameFieldsProcessorFieldsItems]

        :param id: The ``RenameFieldsProcessor`` ``id``.
        :type id: str

        :param inputs: The ``RenameFieldsProcessor`` ``inputs``.
        :type inputs: [str]

        :param type: The definition of ``RenameFieldsProcessorType`` object.
        :type type: RenameFieldsProcessorType
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.id = id
        self_.inputs = inputs
        self_.type = type
