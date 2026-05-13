# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity import Entity
    from datadog_api_client.v2.model.workflow_instance_summary_attributes_status import (
        WorkflowInstanceSummaryAttributesStatus,
    )


class WorkflowInstanceSummaryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity import Entity
        from datadog_api_client.v2.model.workflow_instance_summary_attributes_status import (
            WorkflowInstanceSummaryAttributesStatus,
        )

        return {
            "created_at": (datetime,),
            "entities": ([Entity],),
            "status": (WorkflowInstanceSummaryAttributesStatus,),
            "status_display": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "entities": "entities",
        "status": "status",
        "status_display": "status_display",
    }

    def __init__(
        self_,
        created_at: datetime,
        entities: List[Entity],
        status: WorkflowInstanceSummaryAttributesStatus,
        status_display: str,
        **kwargs,
    ):
        """
        Attributes of a workflow instance summary.

        :param created_at: Timestamp when the workflow instance was created.
        :type created_at: datetime

        :param entities: The entities being processed by this workflow instance.
        :type entities: [Entity]

        :param status: The current status of the step.
        :type status: WorkflowInstanceSummaryAttributesStatus

        :param status_display: A human-readable display name for the current status.
        :type status_display: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.entities = entities
        self_.status = status
        self_.status_display = status_display
