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
    from datadog_api_client.v2.model.workflow_headless_execution_config import WorkflowHeadlessExecutionConfig


class WorkflowHeadlessExecutionRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_headless_execution_config import WorkflowHeadlessExecutionConfig

        return {
            "config": (WorkflowHeadlessExecutionConfig,),
            "template_id": (str,),
        }

    attribute_map = {
        "config": "config",
        "template_id": "template_id",
    }

    def __init__(self_, config: WorkflowHeadlessExecutionConfig, template_id: str, **kwargs):
        """


        :param config:
        :type config: WorkflowHeadlessExecutionConfig

        :param template_id: The ID of the workflow template to execute
        :type template_id: str
        """
        super().__init__(kwargs)

        self_.config = config
        self_.template_id = template_id
