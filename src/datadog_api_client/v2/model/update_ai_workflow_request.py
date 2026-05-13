# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity import Entity
    from datadog_api_client.v2.model.filtering_logic import FilteringLogic


class UpdateAIWorkflowRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity import Entity
        from datadog_api_client.v2.model.filtering_logic import FilteringLogic

        return {
            "completed_at": (datetime,),
            "entities": ([[Entity]],),
            "filtering_logic": (FilteringLogic,),
            "grouping_logic": (str,),
            "max_number_of_entities_per_session": (int,),
            "prompt": (str,),
            "repository": (str,),
            "workflow_name": (str,),
        }

    attribute_map = {
        "completed_at": "completed_at",
        "entities": "entities",
        "filtering_logic": "filtering_logic",
        "grouping_logic": "grouping_logic",
        "max_number_of_entities_per_session": "max_number_of_entities_per_session",
        "prompt": "prompt",
        "repository": "repository",
        "workflow_name": "workflow_name",
    }

    def __init__(
        self_,
        completed_at: Union[datetime, UnsetType] = unset,
        entities: Union[List[List[Entity]], UnsetType] = unset,
        filtering_logic: Union[FilteringLogic, UnsetType] = unset,
        grouping_logic: Union[str, UnsetType] = unset,
        max_number_of_entities_per_session: Union[int, UnsetType] = unset,
        prompt: Union[str, UnsetType] = unset,
        repository: Union[str, UnsetType] = unset,
        workflow_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request body for updating an existing AI workflow. All fields are optional.

        :param completed_at: Timestamp marking when the workflow completed.
        :type completed_at: datetime, optional

        :param entities: A list of entity groups. Each group is processed in a separate workflow execution.
        :type entities: [[Entity]], optional

        :param filtering_logic: Arbitrary filtering criteria used to select entities for the workflow.
        :type filtering_logic: FilteringLogic, optional

        :param grouping_logic: Updated entity grouping logic.
        :type grouping_logic: str, optional

        :param max_number_of_entities_per_session: Updated maximum number of entities per execution session.
        :type max_number_of_entities_per_session: int, optional

        :param prompt: Updated AI prompt for the workflow.
        :type prompt: str, optional

        :param repository: Updated target repository in owner/repo format.
        :type repository: str, optional

        :param workflow_name: Updated name for the workflow.
        :type workflow_name: str, optional
        """
        if completed_at is not unset:
            kwargs["completed_at"] = completed_at
        if entities is not unset:
            kwargs["entities"] = entities
        if filtering_logic is not unset:
            kwargs["filtering_logic"] = filtering_logic
        if grouping_logic is not unset:
            kwargs["grouping_logic"] = grouping_logic
        if max_number_of_entities_per_session is not unset:
            kwargs["max_number_of_entities_per_session"] = max_number_of_entities_per_session
        if prompt is not unset:
            kwargs["prompt"] = prompt
        if repository is not unset:
            kwargs["repository"] = repository
        if workflow_name is not unset:
            kwargs["workflow_name"] = workflow_name
        super().__init__(kwargs)
