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


class ScaRequestDataAttributesCommit(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "author_date": (str,),
            "author_email": (str,),
            "author_name": (str,),
            "branch": (str,),
            "committer_email": (str,),
            "committer_name": (str,),
            "sha": (str,),
        }

    attribute_map = {
        "author_date": "author_date",
        "author_email": "author_email",
        "author_name": "author_name",
        "branch": "branch",
        "committer_email": "committer_email",
        "committer_name": "committer_name",
        "sha": "sha",
    }

    def __init__(
        self_,
        author_date: Union[str, UnsetType] = unset,
        author_email: Union[str, UnsetType] = unset,
        author_name: Union[str, UnsetType] = unset,
        branch: Union[str, UnsetType] = unset,
        committer_email: Union[str, UnsetType] = unset,
        committer_name: Union[str, UnsetType] = unset,
        sha: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the commit associated with the SCA scan, including author, committer, and branch information.

        :param author_date: The date when the commit was authored.
        :type author_date: str, optional

        :param author_email: The email address of the commit author.
        :type author_email: str, optional

        :param author_name: The full name of the commit author.
        :type author_name: str, optional

        :param branch: The branch name on which the commit was made.
        :type branch: str, optional

        :param committer_email: The email address of the person who committed the change.
        :type committer_email: str, optional

        :param committer_name: The full name of the person who committed the change.
        :type committer_name: str, optional

        :param sha: The SHA hash uniquely identifying the commit.
        :type sha: str, optional
        """
        if author_date is not unset:
            kwargs["author_date"] = author_date
        if author_email is not unset:
            kwargs["author_email"] = author_email
        if author_name is not unset:
            kwargs["author_name"] = author_name
        if branch is not unset:
            kwargs["branch"] = branch
        if committer_email is not unset:
            kwargs["committer_email"] = committer_email
        if committer_name is not unset:
            kwargs["committer_name"] = committer_name
        if sha is not unset:
            kwargs["sha"] = sha
        super().__init__(kwargs)
