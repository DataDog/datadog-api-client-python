# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IssueSampleGitFileLocation(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "column": (int,),
            "filepath": (str,),
            "first_line": (int,),
            "last_line": (int,),
            "ref": (str,),
            "repo_id": (str,),
        }

    attribute_map = {
        "column": "column",
        "filepath": "filepath",
        "first_line": "first_line",
        "last_line": "last_line",
        "ref": "ref",
        "repo_id": "repo_id",
    }

    def __init__(
        self_,
        column: Union[int, UnsetType] = unset,
        filepath: Union[str, UnsetType] = unset,
        first_line: Union[int, UnsetType] = unset,
        last_line: Union[int, UnsetType] = unset,
        ref: Union[str, UnsetType] = unset,
        repo_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Location of a stack frame in a repository file. Empty when the source code is unavailable.

        :param column: Column of the location, starting at 1.
        :type column: int, optional

        :param filepath: Path of the file in the repository.
        :type filepath: str, optional

        :param first_line: First line of the location, starting at 1.
        :type first_line: int, optional

        :param last_line: Last line of the location, starting at 1.
        :type last_line: int, optional

        :param ref: Git reference of the file, usually a commit SHA.
        :type ref: str, optional

        :param repo_id: Repository identifier.
        :type repo_id: str, optional
        """
        if column is not unset:
            kwargs["column"] = column
        if filepath is not unset:
            kwargs["filepath"] = filepath
        if first_line is not unset:
            kwargs["first_line"] = first_line
        if last_line is not unset:
            kwargs["last_line"] = last_line
        if ref is not unset:
            kwargs["ref"] = ref
        if repo_id is not unset:
            kwargs["repo_id"] = repo_id
        super().__init__(kwargs)
