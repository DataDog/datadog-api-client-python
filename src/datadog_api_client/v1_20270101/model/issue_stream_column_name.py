# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueStreamColumnName(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["service", "count", "volume", "resources", "error_type", "error_message", "file_path", "last_seen", "first_seen", "language", "platform", "details", "impacted_sessions", "impacted_users"].
    :type value: str
    """

    allowed_values = {
        "service",
        "count",
        "volume",
        "resources",
        "error_type",
        "error_message",
        "file_path",
        "last_seen",
        "first_seen",
        "language",
        "platform",
        "details",
        "impacted_sessions",
        "impacted_users",
    }
    SERVICE: ClassVar["IssueStreamColumnName"]
    COUNT: ClassVar["IssueStreamColumnName"]
    VOLUME: ClassVar["IssueStreamColumnName"]
    RESOURCES: ClassVar["IssueStreamColumnName"]
    ERROR_TYPE: ClassVar["IssueStreamColumnName"]
    ERROR_MESSAGE: ClassVar["IssueStreamColumnName"]
    FILE_PATH: ClassVar["IssueStreamColumnName"]
    LAST_SEEN: ClassVar["IssueStreamColumnName"]
    FIRST_SEEN: ClassVar["IssueStreamColumnName"]
    LANGUAGE: ClassVar["IssueStreamColumnName"]
    PLATFORM: ClassVar["IssueStreamColumnName"]
    DETAILS: ClassVar["IssueStreamColumnName"]
    IMPACTED_SESSIONS: ClassVar["IssueStreamColumnName"]
    IMPACTED_USERS: ClassVar["IssueStreamColumnName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueStreamColumnName.SERVICE = IssueStreamColumnName("service")
IssueStreamColumnName.COUNT = IssueStreamColumnName("count")
IssueStreamColumnName.VOLUME = IssueStreamColumnName("volume")
IssueStreamColumnName.RESOURCES = IssueStreamColumnName("resources")
IssueStreamColumnName.ERROR_TYPE = IssueStreamColumnName("error_type")
IssueStreamColumnName.ERROR_MESSAGE = IssueStreamColumnName("error_message")
IssueStreamColumnName.FILE_PATH = IssueStreamColumnName("file_path")
IssueStreamColumnName.LAST_SEEN = IssueStreamColumnName("last_seen")
IssueStreamColumnName.FIRST_SEEN = IssueStreamColumnName("first_seen")
IssueStreamColumnName.LANGUAGE = IssueStreamColumnName("language")
IssueStreamColumnName.PLATFORM = IssueStreamColumnName("platform")
IssueStreamColumnName.DETAILS = IssueStreamColumnName("details")
IssueStreamColumnName.IMPACTED_SESSIONS = IssueStreamColumnName("impacted_sessions")
IssueStreamColumnName.IMPACTED_USERS = IssueStreamColumnName("impacted_users")
