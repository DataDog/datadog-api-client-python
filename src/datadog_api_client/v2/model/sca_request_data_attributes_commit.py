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


        :param author_date:
        :type author_date: str, optional

        :param author_email:
        :type author_email: str, optional

        :param author_name:
        :type author_name: str, optional

        :param branch:
        :type branch: str, optional

        :param committer_email:
        :type committer_email: str, optional

        :param committer_name:
        :type committer_name: str, optional

        :param sha:
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
