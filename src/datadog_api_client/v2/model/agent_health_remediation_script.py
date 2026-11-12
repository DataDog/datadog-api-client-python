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


class AgentHealthRemediationScript(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "content": (str,),
            "filename": (str,),
            "language": (str,),
            "language_version": (str,),
            "requires_root": (bool,),
        }

    attribute_map = {
        "content": "content",
        "filename": "filename",
        "language": "language",
        "language_version": "language_version",
        "requires_root": "requires_root",
    }

    def __init__(
        self_,
        content: Union[str, UnsetType] = unset,
        filename: Union[str, UnsetType] = unset,
        language: Union[str, UnsetType] = unset,
        language_version: Union[str, UnsetType] = unset,
        requires_root: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        A script that can be used to remediate the issue.

        :param content: The content of the script.
        :type content: str, optional

        :param filename: The filename of the script.
        :type filename: str, optional

        :param language: The language of the script.
        :type language: str, optional

        :param language_version: The language version used by the script.
        :type language_version: str, optional

        :param requires_root: Whether the script requires root privileges.
        :type requires_root: bool, optional
        """
        if content is not unset:
            kwargs["content"] = content
        if filename is not unset:
            kwargs["filename"] = filename
        if language is not unset:
            kwargs["language"] = language
        if language_version is not unset:
            kwargs["language_version"] = language_version
        if requires_root is not unset:
            kwargs["requires_root"] = requires_root
        super().__init__(kwargs)
