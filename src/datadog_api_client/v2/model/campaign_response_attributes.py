# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class CampaignResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "description": (str,),
            "due_date": (datetime,),
            "entity_scope": (str,),
            "guidance": (str,),
            "key": (str,),
            "modified_at": (datetime,),
            "name": (str,),
            "owner": (str,),
            "start_date": (datetime,),
            "status": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "due_date": "due_date",
        "entity_scope": "entity_scope",
        "guidance": "guidance",
        "key": "key",
        "modified_at": "modified_at",
        "name": "name",
        "owner": "owner",
        "start_date": "start_date",
        "status": "status",
    }

    def __init__(
        self_,
        created_at: datetime,
        key: str,
        modified_at: datetime,
        name: str,
        owner: str,
        start_date: datetime,
        status: str,
        description: Union[str, UnsetType] = unset,
        due_date: Union[datetime, UnsetType] = unset,
        entity_scope: Union[str, UnsetType] = unset,
        guidance: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Campaign attributes.

        :param created_at: Creation time of the campaign.
        :type created_at: datetime

        :param description: The description of the campaign.
        :type description: str, optional

        :param due_date: The due date of the campaign.
        :type due_date: datetime, optional

        :param entity_scope: Entity scope query to filter entities for this campaign.
        :type entity_scope: str, optional

        :param guidance: Guidance for the campaign.
        :type guidance: str, optional

        :param key: The unique key for the campaign.
        :type key: str

        :param modified_at: Time of last campaign modification.
        :type modified_at: datetime

        :param name: The name of the campaign.
        :type name: str

        :param owner: The UUID of the campaign owner.
        :type owner: str

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
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.key = key
        self_.modified_at = modified_at
        self_.name = name
        self_.owner = owner
        self_.start_date = start_date
        self_.status = status
