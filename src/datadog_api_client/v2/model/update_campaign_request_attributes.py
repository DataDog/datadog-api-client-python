# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class UpdateCampaignRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "due_date": (datetime,),
            "entity_scope": (str,),
            "guidance": (str,),
            "key": (str,),
            "name": (str,),
            "owner_id": (str,),
            "rule_ids": ([str],),
            "start_date": (datetime,),
            "status": (str,),
        }

    attribute_map = {
        "description": "description",
        "due_date": "due_date",
        "entity_scope": "entity_scope",
        "guidance": "guidance",
        "key": "key",
        "name": "name",
        "owner_id": "owner_id",
        "rule_ids": "rule_ids",
        "start_date": "start_date",
        "status": "status",
    }

    def __init__(
        self_,
        name: str,
        owner_id: str,
        rule_ids: List[str],
        start_date: datetime,
        status: str,
        description: Union[str, UnsetType] = unset,
        due_date: Union[datetime, UnsetType] = unset,
        entity_scope: Union[str, UnsetType] = unset,
        guidance: Union[str, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a campaign.

        :param description: The description of the campaign.
        :type description: str, optional

        :param due_date: The due date of the campaign.
        :type due_date: datetime, optional

        :param entity_scope: Entity scope query to filter entities for this campaign.
        :type entity_scope: str, optional

        :param guidance: Guidance for the campaign.
        :type guidance: str, optional

        :param key: The unique key for the campaign.
        :type key: str, optional

        :param name: The name of the campaign.
        :type name: str

        :param owner_id: The UUID of the campaign owner.
        :type owner_id: str

        :param rule_ids: Array of rule IDs associated with this campaign.
        :type rule_ids: [str]

        :param start_date: The start date of the campaign.
        :type start_date: datetime

        :param status: The status of the campaign.
        :type status: str
        """
        if description is not unset:
            kwargs["description"] = description
        if due_date is not unset:
            kwargs["due_date"] = due_date
        if entity_scope is not unset:
            kwargs["entity_scope"] = entity_scope
        if guidance is not unset:
            kwargs["guidance"] = guidance
        if key is not unset:
            kwargs["key"] = key
        super().__init__(kwargs)

        self_.name = name
        self_.owner_id = owner_id
        self_.rule_ids = rule_ids
        self_.start_date = start_date
        self_.status = status
