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
    from datadog_api_client.v2.model.input_schema_data import InputSchemaData


class InputSchema(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.input_schema_data import InputSchemaData

        return {
            "data": (InputSchemaData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[InputSchemaData, UnsetType] = unset, **kwargs):
        """
        The definition of ``InputSchema`` object.

        :param data: The definition of ``InputSchemaData`` object.
        :type data: InputSchemaData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
