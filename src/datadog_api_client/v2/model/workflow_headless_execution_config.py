# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.workflow_headless_execution_connection import WorkflowHeadlessExecutionConnection


class WorkflowHeadlessExecutionConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_headless_execution_connection import (
            WorkflowHeadlessExecutionConnection,
        )

        return {
            "connections": ([WorkflowHeadlessExecutionConnection],),
            "inputs": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
        }

    attribute_map = {
        "connections": "connections",
        "inputs": "inputs",
    }

    def __init__(self_, connections: List[WorkflowHeadlessExecutionConnection], inputs: Dict[str, Any], **kwargs):
        """


        :param connections: List of connections to use for the workflow execution
        :type connections: [WorkflowHeadlessExecutionConnection]

        :param inputs: Input parameters for the workflow execution
        :type inputs: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}
        """
        super().__init__(kwargs)

        self_.connections = connections
        self_.inputs = inputs
