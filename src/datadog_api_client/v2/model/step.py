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
    from datadog_api_client.v2.model.completion_gate import CompletionGate
    from datadog_api_client.v2.model.step_display import StepDisplay
    from datadog_api_client.v2.model.error_handler import ErrorHandler
    from datadog_api_client.v2.model.outbound_edge import OutboundEdge
    from datadog_api_client.v2.model.parameter import Parameter
    from datadog_api_client.v2.model.readiness_gate import ReadinessGate


class Step(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.completion_gate import CompletionGate
        from datadog_api_client.v2.model.step_display import StepDisplay
        from datadog_api_client.v2.model.error_handler import ErrorHandler
        from datadog_api_client.v2.model.outbound_edge import OutboundEdge
        from datadog_api_client.v2.model.parameter import Parameter
        from datadog_api_client.v2.model.readiness_gate import ReadinessGate

        return {
            "action_id": (str,),
            "completion_gate": (CompletionGate,),
            "connection_label": (str,),
            "display": (StepDisplay,),
            "error_handlers": ([ErrorHandler],),
            "name": (str,),
            "outbound_edges": ([OutboundEdge],),
            "parameters": ([Parameter],),
            "readiness_gate": (ReadinessGate,),
        }

    attribute_map = {
        "action_id": "actionId",
        "completion_gate": "completionGate",
        "connection_label": "connectionLabel",
        "display": "display",
        "error_handlers": "errorHandlers",
        "name": "name",
        "outbound_edges": "outboundEdges",
        "parameters": "parameters",
        "readiness_gate": "readinessGate",
    }

    def __init__(
        self_,
        action_id: str,
        name: str,
        completion_gate: Union[CompletionGate, UnsetType] = unset,
        connection_label: Union[str, UnsetType] = unset,
        display: Union[StepDisplay, UnsetType] = unset,
        error_handlers: Union[List[ErrorHandler], UnsetType] = unset,
        outbound_edges: Union[List[OutboundEdge], UnsetType] = unset,
        parameters: Union[List[Parameter], UnsetType] = unset,
        readiness_gate: Union[ReadinessGate, UnsetType] = unset,
        **kwargs,
    ):
        """
        A Step is a sub-component of a workflow. Each Step performs an action.

        :param action_id: The unique identifier of an action.
        :type action_id: str

        :param completion_gate: Used to create conditions before running subsequent actions.
        :type completion_gate: CompletionGate, optional

        :param connection_label: The unique identifier of a connection defined in the spec.
        :type connection_label: str, optional

        :param display: The definition of ``StepDisplay`` object.
        :type display: StepDisplay, optional

        :param error_handlers: The ``Step`` ``errorHandlers``.
        :type error_handlers: [ErrorHandler], optional

        :param name: Name of the step.
        :type name: str

        :param outbound_edges: A list of subsequent actions to run.
        :type outbound_edges: [OutboundEdge], optional

        :param parameters: A list of inputs for an action.
        :type parameters: [Parameter], optional

        :param readiness_gate: Used to merge multiple branches into a single branch.
        :type readiness_gate: ReadinessGate, optional
        """
        if completion_gate is not unset:
            kwargs["completion_gate"] = completion_gate
        if connection_label is not unset:
            kwargs["connection_label"] = connection_label
        if display is not unset:
            kwargs["display"] = display
        if error_handlers is not unset:
            kwargs["error_handlers"] = error_handlers
        if outbound_edges is not unset:
            kwargs["outbound_edges"] = outbound_edges
        if parameters is not unset:
            kwargs["parameters"] = parameters
        if readiness_gate is not unset:
            kwargs["readiness_gate"] = readiness_gate
        super().__init__(kwargs)

        self_.action_id = action_id
        self_.name = name
