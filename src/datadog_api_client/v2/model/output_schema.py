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
    from datadog_api_client.v2.model.output_schema_parameters import OutputSchemaParameters


class OutputSchema(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.output_schema_parameters import OutputSchemaParameters

        return {
            "parameters": ([OutputSchemaParameters],),
        }

    attribute_map = {
        "parameters": "parameters",
    }

    def __init__(self_, parameters: Union[List[OutputSchemaParameters], UnsetType] = unset, **kwargs):
        """
        A list of output parameters for the workflow.

        :param parameters: The ``OutputSchema`` ``parameters``.
        :type parameters: [OutputSchemaParameters], optional
        """
        if parameters is not unset:
            kwargs["parameters"] = parameters
        super().__init__(kwargs)
