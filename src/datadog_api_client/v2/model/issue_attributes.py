# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue_language import IssueLanguage
    from datadog_api_client.v2.model.issue_platform import IssuePlatform
    from datadog_api_client.v2.model.issue_state import IssueState


class IssueAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_language import IssueLanguage
        from datadog_api_client.v2.model.issue_platform import IssuePlatform
        from datadog_api_client.v2.model.issue_state import IssueState

        return {
            "error_message": (str,),
            "error_type": (str,),
            "file_path": (str,),
            "first_seen": (int,),
            "first_seen_version": (str,),
            "function_name": (str,),
            "is_crash": (bool,),
            "languages": ([IssueLanguage],),
            "last_seen": (int,),
            "last_seen_version": (str,),
            "platform": (IssuePlatform,),
            "service": (str,),
            "state": (IssueState,),
        }

    attribute_map = {
        "error_message": "error_message",
        "error_type": "error_type",
        "file_path": "file_path",
        "first_seen": "first_seen",
        "first_seen_version": "first_seen_version",
        "function_name": "function_name",
        "is_crash": "is_crash",
        "languages": "languages",
        "last_seen": "last_seen",
        "last_seen_version": "last_seen_version",
        "platform": "platform",
        "service": "service",
        "state": "state",
    }

    def __init__(
        self_,
        error_message: Union[str, UnsetType] = unset,
        error_type: Union[str, UnsetType] = unset,
        file_path: Union[str, UnsetType] = unset,
        first_seen: Union[int, UnsetType] = unset,
        first_seen_version: Union[str, UnsetType] = unset,
        function_name: Union[str, UnsetType] = unset,
        is_crash: Union[bool, UnsetType] = unset,
        languages: Union[List[IssueLanguage], UnsetType] = unset,
        last_seen: Union[int, UnsetType] = unset,
        last_seen_version: Union[str, UnsetType] = unset,
        platform: Union[IssuePlatform, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        state: Union[IssueState, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the information of an issue.

        :param error_message: Error message associated with the issue.
        :type error_message: str, optional

        :param error_type: Type of the error that matches the issue.
        :type error_type: str, optional

        :param file_path: Path of the file where the issue occurred.
        :type file_path: str, optional

        :param first_seen: Timestamp of the first seen error in milliseconds since the Unix epoch.
        :type first_seen: int, optional

        :param first_seen_version: The application version (for example, git commit hash) where the issue was first observed.
        :type first_seen_version: str, optional

        :param function_name: Name of the function where the issue occurred.
        :type function_name: str, optional

        :param is_crash: Error is a crash.
        :type is_crash: bool, optional

        :param languages: Array of programming languages associated with the issue.
        :type languages: [IssueLanguage], optional

        :param last_seen: Timestamp of the last seen error in milliseconds since the Unix epoch.
        :type last_seen: int, optional

        :param last_seen_version: The application version (for example, git commit hash) where the issue was last observed.
        :type last_seen_version: str, optional

        :param platform: Platform associated with the issue.
        :type platform: IssuePlatform, optional

        :param service: Service name.
        :type service: str, optional

        :param state: State of the issue
        :type state: IssueState, optional
        """
        if error_message is not unset:
            kwargs["error_message"] = error_message
        if error_type is not unset:
            kwargs["error_type"] = error_type
        if file_path is not unset:
            kwargs["file_path"] = file_path
        if first_seen is not unset:
            kwargs["first_seen"] = first_seen
        if first_seen_version is not unset:
            kwargs["first_seen_version"] = first_seen_version
        if function_name is not unset:
            kwargs["function_name"] = function_name
        if is_crash is not unset:
            kwargs["is_crash"] = is_crash
        if languages is not unset:
            kwargs["languages"] = languages
        if last_seen is not unset:
            kwargs["last_seen"] = last_seen
        if last_seen_version is not unset:
            kwargs["last_seen_version"] = last_seen_version
        if platform is not unset:
            kwargs["platform"] = platform
        if service is not unset:
            kwargs["service"] = service
        if state is not unset:
            kwargs["state"] = state
        super().__init__(kwargs)
