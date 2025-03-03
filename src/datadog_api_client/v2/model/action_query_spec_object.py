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
    from datadog_api_client.v2.model.action_query_spec_connection_group import ActionQuerySpecConnectionGroup
    from datadog_api_client.v2.model.action_query_spec_inputs import ActionQuerySpecInputs
    from datadog_api_client.v2.model.action_query_spec_input import ActionQuerySpecInput


class ActionQuerySpecObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_query_spec_connection_group import ActionQuerySpecConnectionGroup
        from datadog_api_client.v2.model.action_query_spec_inputs import ActionQuerySpecInputs

        return {
            "connection_group": (ActionQuerySpecConnectionGroup,),
            "connection_id": (str,),
            "fqn": (str,),
            "inputs": (ActionQuerySpecInputs,),
        }

    attribute_map = {
        "connection_group": "connectionGroup",
        "connection_id": "connectionId",
        "fqn": "fqn",
        "inputs": "inputs",
    }

    def __init__(
        self_,
        fqn: str,
        connection_group: Union[ActionQuerySpecConnectionGroup, UnsetType] = unset,
        connection_id: Union[str, UnsetType] = unset,
        inputs: Union[ActionQuerySpecInputs, str, ActionQuerySpecInput, UnsetType] = unset,
        **kwargs,
    ):
        """
        The action query spec object.

        :param connection_group: The connection group to use for an action query.
        :type connection_group: ActionQuerySpecConnectionGroup, optional

        :param connection_id: The ID of the custom connection to use for this action query.
        :type connection_id: str, optional

        :param fqn: The fully qualified name of the action type.
        :type fqn: str

        :param inputs: The inputs to the action query. These are the values that are passed to the action when it is triggered.
        :type inputs: ActionQuerySpecInputs, optional
        """
        if connection_group is not unset:
            kwargs["connection_group"] = connection_group
        if connection_id is not unset:
            kwargs["connection_id"] = connection_id
        if inputs is not unset:
            kwargs["inputs"] = inputs
        super().__init__(kwargs)

        self_.fqn = fqn
