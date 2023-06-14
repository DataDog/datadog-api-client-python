# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class CIAppGitInfo(ModelNormal):
    validations = {
        "sha": {},
    }
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "author_email": (str,),
            "author_name": (str, none_type),
            "author_time": (str, none_type),
            "branch": (str, none_type),
            "commit_time": (str, none_type),
            "committer_email": (str, none_type),
            "committer_name": (str, none_type),
            "default_branch": (str, none_type),
            "message": (str, none_type),
            "repository_url": (str,),
            "sha": (str,),
            "tag": (str, none_type),
        }

    attribute_map = {
        "author_email": "author_email",
        "author_name": "author_name",
        "author_time": "author_time",
        "branch": "branch",
        "commit_time": "commit_time",
        "committer_email": "committer_email",
        "committer_name": "committer_name",
        "default_branch": "default_branch",
        "message": "message",
        "repository_url": "repository_url",
        "sha": "sha",
        "tag": "tag",
    }

    def __init__(
        self_,
        author_email: str,
        repository_url: str,
        sha: str,
        author_name: Union[str, none_type, UnsetType] = unset,
        author_time: Union[str, none_type, UnsetType] = unset,
        branch: Union[str, none_type, UnsetType] = unset,
        commit_time: Union[str, none_type, UnsetType] = unset,
        committer_email: Union[str, none_type, UnsetType] = unset,
        committer_name: Union[str, none_type, UnsetType] = unset,
        default_branch: Union[str, none_type, UnsetType] = unset,
        message: Union[str, none_type, UnsetType] = unset,
        tag: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        If pipelines are triggered due to actions to a Git repository, then all payloads must contain this.
        Note that either ``tag`` or ``branch`` has to be provided, but not both.

        :param author_email: The commit author email.
        :type author_email: str

        :param author_name: The commit author name.
        :type author_name: str, none_type, optional

        :param author_time: The commit author timestamp in RFC3339 format.
        :type author_time: str, none_type, optional

        :param branch: The branch name (if a tag use the tag parameter).
        :type branch: str, none_type, optional

        :param commit_time: The commit timestamp in RFC3339 format.
        :type commit_time: str, none_type, optional

        :param committer_email: The committer email.
        :type committer_email: str, none_type, optional

        :param committer_name: The committer name.
        :type committer_name: str, none_type, optional

        :param default_branch: The Git repository's default branch.
        :type default_branch: str, none_type, optional

        :param message: The commit message.
        :type message: str, none_type, optional

        :param repository_url: The URL of the repository.
        :type repository_url: str

        :param sha: The git commit SHA.
        :type sha: str

        :param tag: The tag name (if a branch use the branch parameter).
        :type tag: str, none_type, optional
        """
        if author_name is not unset:
            kwargs["author_name"] = author_name
        if author_time is not unset:
            kwargs["author_time"] = author_time
        if branch is not unset:
            kwargs["branch"] = branch
        if commit_time is not unset:
            kwargs["commit_time"] = commit_time
        if committer_email is not unset:
            kwargs["committer_email"] = committer_email
        if committer_name is not unset:
            kwargs["committer_name"] = committer_name
        if default_branch is not unset:
            kwargs["default_branch"] = default_branch
        if message is not unset:
            kwargs["message"] = message
        if tag is not unset:
            kwargs["tag"] = tag
        super().__init__(kwargs)

        self_.author_email = author_email
        self_.repository_url = repository_url
        self_.sha = sha
