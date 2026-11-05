# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AiGatewayModelModalities(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "input": ([str],),
            "output": ([str],),
        }

    attribute_map = {
        "input": "input",
        "output": "output",
    }

    def __init__(
        self_, input: Union[List[str], UnsetType] = unset, output: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Supported model input and output modalities.

        :param input:
        :type input: [str], optional

        :param output:
        :type output: [str], optional
        """
        if input is not unset:
            kwargs["input"] = input
        if output is not unset:
            kwargs["output"] = output
        super().__init__(kwargs)
