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


class ScorecardListResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "description": (str,),
            "modified_at": (datetime,),
            "name": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "modified_at": "modified_at",
        "name": "name",
    }

    def __init__(
        self_,
        created_at: datetime,
        modified_at: datetime,
        name: str,
        description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Scorecard attributes.

        :param created_at: Creation time of the scorecard.
        :type created_at: datetime

        :param description: The description of the scorecard.
        :type description: str, optional

        :param modified_at: Time of last scorecard modification.
        :type modified_at: datetime

        :param name: The name of the scorecard.
        :type name: str
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.modified_at = modified_at
        self_.name = name
