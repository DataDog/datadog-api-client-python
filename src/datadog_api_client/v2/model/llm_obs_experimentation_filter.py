# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class LLMObsExperimentationFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "include_deleted": (bool,),
            "is_deleted": (bool,),
            "query": (str,),
            "scope": ([str],),
            "version": (int, none_type),
        }

    attribute_map = {
        "include_deleted": "include_deleted",
        "is_deleted": "is_deleted",
        "query": "query",
        "scope": "scope",
        "version": "version",
    }

    def __init__(
        self_,
        scope: List[str],
        include_deleted: Union[bool, UnsetType] = unset,
        is_deleted: Union[bool, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        version: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Filter criteria for an experimentation search request.

        :param include_deleted: When ``true`` , include soft-deleted entities alongside active ones.
        :type include_deleted: bool, optional

        :param is_deleted: When ``true`` , return only soft-deleted entities.
        :type is_deleted: bool, optional

        :param query: Free-text search query.
        :type query: str, optional

        :param scope: Entity types to search. Valid values are ``projects`` , ``datasets`` , ``dataset_records`` , ``experiments`` , and ``experiment_runs``.
        :type scope: [str]

        :param version: Filter dataset records by a specific dataset version.
        :type version: int, none_type, optional
        """
        if include_deleted is not unset:
            kwargs["include_deleted"] = include_deleted
        if is_deleted is not unset:
            kwargs["is_deleted"] = is_deleted
        if query is not unset:
            kwargs["query"] = query
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.scope = scope
