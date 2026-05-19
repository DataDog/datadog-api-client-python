# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class CaseTypeResourceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "deleted_at": (datetime, none_type),
            "description": (str,),
            "emoji": (str,),
            "name": (str,),
        }

    attribute_map = {
        "deleted_at": "deleted_at",
        "description": "description",
        "emoji": "emoji",
        "name": "name",
    }
    read_only_vars = {
        "deleted_at",
    }

    def __init__(
        self_,
        name: str,
        deleted_at: Union[datetime, none_type, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        emoji: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a case type, which define a classification category for cases. Organizations use case types to model different workflows (for example, Security Incident, Bug Report, Change Request).

        :param deleted_at: Timestamp when the case type was marked as deleted. A null value indicates the case type is active.
        :type deleted_at: datetime, none_type, optional

        :param description: A detailed description explaining when this case type should be used.
        :type description: str, optional

        :param emoji: An emoji icon representing the case type in the UI.
        :type emoji: str, optional

        :param name: The display name of the case type, shown in the Case Management UI when creating or viewing cases.
        :type name: str
        """
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        if description is not unset:
            kwargs["description"] = description
        if emoji is not unset:
            kwargs["emoji"] = emoji
        super().__init__(kwargs)

        self_.name = name
