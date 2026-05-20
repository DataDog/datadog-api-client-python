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


class MaintenanceWindowAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_by": (str,),
            "end_at": (datetime,),
            "name": (str,),
            "query": (str,),
            "start_at": (datetime,),
            "updated_by": (str,),
        }

    attribute_map = {
        "created_by": "created_by",
        "end_at": "end_at",
        "name": "name",
        "query": "query",
        "start_at": "start_at",
        "updated_by": "updated_by",
    }
    read_only_vars = {
        "created_by",
        "updated_by",
    }

    def __init__(
        self_,
        end_at: datetime,
        name: str,
        query: str,
        start_at: datetime,
        created_by: Union[str, UnsetType] = unset,
        updated_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a maintenance window, including its schedule and the query that determines which cases are affected.

        :param created_by: The UUID of the user who created this maintenance window. Read-only.
        :type created_by: str, optional

        :param end_at: The ISO 8601 timestamp when the maintenance window ends and normal notification behavior resumes.
        :type end_at: datetime

        :param name: A human-readable name for the maintenance window (for example, ``Database migration - Dec 15`` ).
        :type name: str

        :param query: A case search query that determines which cases are affected during the maintenance window. Uses the same syntax as the Case Management search bar.
        :type query: str

        :param start_at: The ISO 8601 timestamp when the maintenance window begins and notifications start being suppressed.
        :type start_at: datetime

        :param updated_by: The UUID of the user who last modified this maintenance window. Read-only.
        :type updated_by: str, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)

        self_.end_at = end_at
        self_.name = name
        self_.query = query
        self_.start_at = start_at
