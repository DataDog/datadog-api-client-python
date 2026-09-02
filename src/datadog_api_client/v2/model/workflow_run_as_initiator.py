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
    from datadog_api_client.v2.model.workflow_run_as_initiator_type import WorkflowRunAsInitiatorType


class WorkflowRunAsInitiator(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_run_as_initiator_type import WorkflowRunAsInitiatorType

        return {
            "type": (WorkflowRunAsInitiatorType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: WorkflowRunAsInitiatorType, **kwargs):
        """
        Run the workflow as the user who initiates the execution.

        :param type: The initiator run-as type.
        :type type: WorkflowRunAsInitiatorType
        """
        super().__init__(kwargs)

        self_.type = type
