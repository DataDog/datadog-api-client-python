# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class FeatureFlagStalenessCodeReference(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "files": ([str],),
            "repo_url": (str,),
            "scm_repository_id": (str,),
        }

    attribute_map = {
        "files": "files",
        "repo_url": "repo_url",
        "scm_repository_id": "scm_repository_id",
    }

    def __init__(
        self_,
        files: Union[List[str], UnsetType] = unset,
        repo_url: Union[str, UnsetType] = unset,
        scm_repository_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A repository and its files that reference the feature flag.

        :param files: Paths of files that reference the feature flag in this repository.
        :type files: [str], optional

        :param repo_url: The URL of the source code repository, when available.
        :type repo_url: str, optional

        :param scm_repository_id: The identifier of the source code repository.
        :type scm_repository_id: str, optional
        """
        if files is not unset:
            kwargs["files"] = files
        if repo_url is not unset:
            kwargs["repo_url"] = repo_url
        if scm_repository_id is not unset:
            kwargs["scm_repository_id"] = scm_repository_id
        super().__init__(kwargs)
