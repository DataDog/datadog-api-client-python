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
    from datadog_api_client.v1_20270101.model.run_workflow_execution_input import RunWorkflowExecutionInput
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.run_workflow_backend_definition_type import (
        RunWorkflowBackendDefinitionType,
    )


class RunWorkflowBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.run_workflow_execution_input import RunWorkflowExecutionInput
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.run_workflow_backend_definition_type import (
            RunWorkflowBackendDefinitionType,
        )

        return {
            "description": (str,),
            "inputs": ([RunWorkflowExecutionInput],),
            "notes": (str,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (RunWorkflowBackendDefinitionType,),
            "workflow_id": (str,),
        }

    attribute_map = {
        "description": "description",
        "inputs": "inputs",
        "notes": "notes",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
        "workflow_id": "workflow_id",
    }

    def __init__(
        self_,
        type: RunWorkflowBackendDefinitionType,
        workflow_id: str,
        description: Union[str, UnsetType] = unset,
        inputs: Union[List[RunWorkflowExecutionInput], UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param inputs: Test-only generated schema for the dashboard versioning proof of concept.
        :type inputs: [RunWorkflowExecutionInput], optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: RunWorkflowBackendDefinitionType

        :param workflow_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type workflow_id: str
        """
        if description is not unset:
            kwargs["description"] = description
        if inputs is not unset:
            kwargs["inputs"] = inputs
        if notes is not unset:
            kwargs["notes"] = notes
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.type = type
        self_.workflow_id = workflow_id
