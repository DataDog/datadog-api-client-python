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
    from datadog_api_client.v2.model.execution_step import ExecutionStep


class ListExecutionStepsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_step import ExecutionStep

        return {
            "steps": ([ExecutionStep],),
        }

    attribute_map = {
        "steps": "steps",
    }

    def __init__(self_, steps: List[ExecutionStep], **kwargs):
        """
        Attributes of an execution steps response.

        :param steps: The list of steps for the workflow execution.
        :type steps: [ExecutionStep]
        """
        super().__init__(kwargs)

        self_.steps = steps
