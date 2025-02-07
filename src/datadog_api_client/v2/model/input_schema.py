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
    from datadog_api_client.v2.model.input_schema_parameters import InputSchemaParameters


class InputSchema(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.input_schema_parameters import InputSchemaParameters

        return {
            "parameters": ([InputSchemaParameters],),
        }

    attribute_map = {
        "parameters": "parameters",
    }

    def __init__(self_, parameters: Union[List[InputSchemaParameters], UnsetType] = unset, **kwargs):
        """
        A list of input parameters for the workflow. These can be used as dynamic runtime values in your workflow.

        :param parameters: The ``InputSchema`` ``parameters``.
        :type parameters: [InputSchemaParameters], optional
        """
        if parameters is not unset:
            kwargs["parameters"] = parameters
        super().__init__(kwargs)
