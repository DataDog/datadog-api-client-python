# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity import Entity


class WorkflowExecutionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity import Entity

        return {
            "ai_workflow_id": (UUID,),
            "created_at": (datetime,),
            "entities": ([Entity],),
            "instance_id": (UUID,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "ai_workflow_id": "ai_workflow_id",
        "created_at": "created_at",
        "entities": "entities",
        "instance_id": "instance_id",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        ai_workflow_id: UUID,
        created_at: datetime,
        entities: List[Entity],
        instance_id: UUID,
        updated_at: datetime,
        **kwargs,
    ):
        """
        Attributes of a workflow execution.

        :param ai_workflow_id: The ID of the parent AI workflow.
        :type ai_workflow_id: UUID

        :param created_at: Timestamp when the execution was created.
        :type created_at: datetime

        :param entities: The list of entities processed by this execution.
        :type entities: [Entity]

        :param instance_id: The Datadog Workflow Automation instance ID for this execution.
        :type instance_id: UUID

        :param updated_at: Timestamp when the execution was last updated.
        :type updated_at: datetime
        """
        super().__init__(kwargs)

        self_.ai_workflow_id = ai_workflow_id
        self_.created_at = created_at
        self_.entities = entities
        self_.instance_id = instance_id
        self_.updated_at = updated_at
