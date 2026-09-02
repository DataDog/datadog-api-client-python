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
    from datadog_api_client.v2.model.workflow_run_as_owner_type import WorkflowRunAsOwnerType


class WorkflowRunAsOwner(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_run_as_owner_type import WorkflowRunAsOwnerType

        return {
            "type": (WorkflowRunAsOwnerType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: WorkflowRunAsOwnerType, **kwargs):
        """
        Run the workflow as its owner.

        :param type: The owner run-as type.
        :type type: WorkflowRunAsOwnerType
        """
        super().__init__(kwargs)

        self_.type = type
