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


class FilesCoverageRequestAttributes(ModelNormal):
    validations = {
        "commit_sha": {},
        "pr_number": {
            "inclusive_minimum": 1,
        },
        "repository_id": {
            "min_length": 1,
        },
        "repository_url": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "branch": (str,),
            "changed_only": (bool,),
            "codeowner": (str,),
            "commit_sha": (str,),
            "flag": (str,),
            "pr_number": (int,),
            "repository_id": (str,),
            "repository_url": (str,),
            "service": (str,),
        }

    attribute_map = {
        "branch": "branch",
        "changed_only": "changed_only",
        "codeowner": "codeowner",
        "commit_sha": "commit_sha",
        "flag": "flag",
        "pr_number": "pr_number",
        "repository_id": "repository_id",
        "repository_url": "repository_url",
        "service": "service",
    }

    def __init__(
        self_,
        branch: Union[str, UnsetType] = unset,
        changed_only: Union[bool, UnsetType] = unset,
        codeowner: Union[str, UnsetType] = unset,
        commit_sha: Union[str, UnsetType] = unset,
        flag: Union[str, UnsetType] = unset,
        pr_number: Union[int, UnsetType] = unset,
        repository_id: Union[str, UnsetType] = unset,
        repository_url: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for requesting per-file code coverage data. Exactly one of ``commit_sha`` , ``branch`` , or ``pr_number`` must be provided. At most one of ``service`` , ``codeowner`` , or ``flag`` may be provided.

        :param branch: The branch name.
        :type branch: str, optional

        :param changed_only: When true, return coverage data only for files that were changed in the specified scope.
        :type changed_only: bool, optional

        :param codeowner: Filter coverage by code owner. At most one of ``service`` , ``codeowner`` , or ``flag`` may be provided.
        :type codeowner: str, optional

        :param commit_sha: The commit SHA (40-character hexadecimal string).
        :type commit_sha: str, optional

        :param flag: Filter coverage by coverage flag. At most one of ``service`` , ``codeowner`` , or ``flag`` may be provided.
        :type flag: str, optional

        :param pr_number: The pull request number. Must be a positive integer.
        :type pr_number: int, optional

        :param repository_id: Deprecated: use ``repository_url`` instead. The repository URL. **Deprecated**.
        :type repository_id: str, optional

        :param repository_url: The repository URL. Accepts a full URL with or without a scheme (for example, ``https://github.com/org/repo`` or ``github.com/org/repo`` ).
        :type repository_url: str, optional

        :param service: Filter coverage by service name. At most one of ``service`` , ``codeowner`` , or ``flag`` may be provided.
        :type service: str, optional
        """
        if branch is not unset:
            kwargs["branch"] = branch
        if changed_only is not unset:
            kwargs["changed_only"] = changed_only
        if codeowner is not unset:
            kwargs["codeowner"] = codeowner
        if commit_sha is not unset:
            kwargs["commit_sha"] = commit_sha
        if flag is not unset:
            kwargs["flag"] = flag
        if pr_number is not unset:
            kwargs["pr_number"] = pr_number
        if repository_id is not unset:
            kwargs["repository_id"] = repository_id
        if repository_url is not unset:
            kwargs["repository_url"] = repository_url
        if service is not unset:
            kwargs["service"] = service
        super().__init__(kwargs)
