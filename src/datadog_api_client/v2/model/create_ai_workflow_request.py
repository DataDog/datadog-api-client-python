# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.filtering_logic import FilteringLogic


class CreateAIWorkflowRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.filtering_logic import FilteringLogic

        return {
            "entities": ([[Entity]],),
            "filtering_logic": (FilteringLogic,),
            "grouping_logic": (str,),
            "idp_campaign_id": (str,),
            "max_number_of_entities_per_session": (int,),
            "prompt": (str,),
            "repository": (str,),
            "user": (str,),
            "workflow_name": (str,),
        }

    attribute_map = {
        "entities": "entities",
        "filtering_logic": "filtering_logic",
        "grouping_logic": "grouping_logic",
        "idp_campaign_id": "idp_campaign_id",
        "max_number_of_entities_per_session": "max_number_of_entities_per_session",
        "prompt": "prompt",
        "repository": "repository",
        "user": "user",
        "workflow_name": "workflow_name",
    }

    def __init__(
        self_,
        entities: List[List[Entity]],
        filtering_logic: FilteringLogic,
        grouping_logic: str,
        idp_campaign_id: str,
        max_number_of_entities_per_session: int,
        prompt: str,
        repository: str,
        user: str,
        workflow_name: str,
        **kwargs,
    ):
        """
        Request body for creating a new AI workflow.

        :param entities: A list of entity groups. Each group is processed in a separate workflow execution.
        :type entities: [[Entity]]

        :param filtering_logic: Arbitrary filtering criteria used to select entities for the workflow.
        :type filtering_logic: FilteringLogic

        :param grouping_logic: The logic used to group entities into batches for execution.
        :type grouping_logic: str

        :param idp_campaign_id: The IDP campaign ID associated with this workflow.
        :type idp_campaign_id: str

        :param max_number_of_entities_per_session: Maximum number of entities allowed per execution session.
        :type max_number_of_entities_per_session: int

        :param prompt: The AI prompt used to guide the dependency upgrade automation.
        :type prompt: str

        :param repository: The target repository in owner/repo format.
        :type repository: str

        :param user: The username of the user initiating the workflow.
        :type user: str

        :param workflow_name: A human-readable name for the workflow.
        :type workflow_name: str
        """
        super().__init__(kwargs)

        self_.entities = entities
        self_.filtering_logic = filtering_logic
        self_.grouping_logic = grouping_logic
        self_.idp_campaign_id = idp_campaign_id
        self_.max_number_of_entities_per_session = max_number_of_entities_per_session
        self_.prompt = prompt
        self_.repository = repository
        self_.user = user
        self_.workflow_name = workflow_name
