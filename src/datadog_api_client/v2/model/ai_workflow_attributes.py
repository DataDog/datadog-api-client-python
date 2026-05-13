# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.filtering_logic import FilteringLogic


class AIWorkflowAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.filtering_logic import FilteringLogic

        return {
            "completed_at": (datetime, none_type),
            "created_at": (datetime,),
            "entities": ([[Entity]],),
            "filtering_logic": (FilteringLogic,),
            "grouping_logic": (str,),
            "idp_campaign_id": (str,),
            "max_number_of_entities_per_session": (int,),
            "prompt": (str,),
            "repository": (str,),
            "updated_at": (datetime,),
            "user": (str,),
            "workflow_id": (UUID,),
            "workflow_name": (str,),
        }

    attribute_map = {
        "completed_at": "completed_at",
        "created_at": "created_at",
        "entities": "entities",
        "filtering_logic": "filtering_logic",
        "grouping_logic": "grouping_logic",
        "idp_campaign_id": "idp_campaign_id",
        "max_number_of_entities_per_session": "max_number_of_entities_per_session",
        "prompt": "prompt",
        "repository": "repository",
        "updated_at": "updated_at",
        "user": "user",
        "workflow_id": "workflow_id",
        "workflow_name": "workflow_name",
    }

    def __init__(
        self_,
        created_at: datetime,
        entities: List[List[Entity]],
        filtering_logic: FilteringLogic,
        grouping_logic: str,
        idp_campaign_id: str,
        max_number_of_entities_per_session: int,
        prompt: str,
        repository: str,
        updated_at: datetime,
        user: str,
        workflow_id: UUID,
        workflow_name: str,
        completed_at: Union[datetime, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an AI workflow.

        :param completed_at: Timestamp when the workflow completed. Null if not yet completed.
        :type completed_at: datetime, none_type, optional

        :param created_at: Timestamp when the workflow was created.
        :type created_at: datetime

        :param entities: A list of entity groups. Each group is processed in a separate workflow execution.
        :type entities: [[Entity]]

        :param filtering_logic: Arbitrary filtering criteria used to select entities for the workflow.
        :type filtering_logic: FilteringLogic

        :param grouping_logic: The logic used to group entities into execution batches.
        :type grouping_logic: str

        :param idp_campaign_id: The IDP campaign ID associated with this workflow.
        :type idp_campaign_id: str

        :param max_number_of_entities_per_session: Maximum number of entities processed in a single execution session.
        :type max_number_of_entities_per_session: int

        :param prompt: The AI prompt guiding the dependency upgrade automation.
        :type prompt: str

        :param repository: The target repository in owner/repo format.
        :type repository: str

        :param updated_at: Timestamp when the workflow was last updated.
        :type updated_at: datetime

        :param user: The username of the user who created the workflow.
        :type user: str

        :param workflow_id: The UUID of the underlying Datadog Workflow Automation workflow.
        :type workflow_id: UUID

        :param workflow_name: The human-readable name of the workflow.
        :type workflow_name: str
        """
        if completed_at is not unset:
            kwargs["completed_at"] = completed_at
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.entities = entities
        self_.filtering_logic = filtering_logic
        self_.grouping_logic = grouping_logic
        self_.idp_campaign_id = idp_campaign_id
        self_.max_number_of_entities_per_session = max_number_of_entities_per_session
        self_.prompt = prompt
        self_.repository = repository
        self_.updated_at = updated_at
        self_.user = user
        self_.workflow_id = workflow_id
        self_.workflow_name = workflow_name
