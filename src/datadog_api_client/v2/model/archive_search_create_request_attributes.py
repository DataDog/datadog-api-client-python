# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.archive_search_create_rehydration import ArchiveSearchCreateRehydration


class ArchiveSearchCreateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.archive_search_create_rehydration import ArchiveSearchCreateRehydration

        return {
            "archive_id": (str,),
            "description": (str,),
            "_from": (datetime,),
            "name": (str,),
            "query": (str,),
            "rehydration": (ArchiveSearchCreateRehydration,),
            "to": (datetime,),
        }

    attribute_map = {
        "archive_id": "archive_id",
        "description": "description",
        "_from": "from",
        "name": "name",
        "query": "query",
        "rehydration": "rehydration",
        "to": "to",
    }

    def __init__(
        self_,
        archive_id: str,
        _from: datetime,
        name: str,
        query: str,
        to: datetime,
        description: Union[str, UnsetType] = unset,
        rehydration: Union[ArchiveSearchCreateRehydration, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes accepted when creating an Archive Search.

        :param archive_id: ID of the archive to search. Use the Logs Archives API to list the archives of the organization.
        :type archive_id: str

        :param description: Free-text description of the Archive Search.
        :type description: str, optional

        :param _from: Start of the time range to search, as an ISO 8601 timestamp.
        :type _from: datetime

        :param name: Name of the Archive Search.
        :type name: str

        :param query: Log search query used to filter the archived logs.
        :type query: str

        :param rehydration: Rehydration settings. Include this object to index the matched logs into a retained historical view.
            Omit it to run an Archive Search that only scans the archive.
        :type rehydration: ArchiveSearchCreateRehydration, optional

        :param to: End of the time range to search, as an ISO 8601 timestamp. Must be after ``from``.
        :type to: datetime
        """
        if description is not unset:
            kwargs["description"] = description
        if rehydration is not unset:
            kwargs["rehydration"] = rehydration
        super().__init__(kwargs)

        self_.archive_id = archive_id
        self_._from = _from
        self_.name = name
        self_.query = query
        self_.to = to
