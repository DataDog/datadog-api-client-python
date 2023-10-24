# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamsField(ModelSimple):
    """
    Supported teams field.

    :param value: Must be one of ["id", "name", "handle", "summary", "description", "avatar", "banner", "visible_modules", "hidden_modules", "created_at", "modified_at", "user_count", "link_count", "team_links", "user_team_permissions"].
    :type value: str
    """

    allowed_values = {
        "id",
        "name",
        "handle",
        "summary",
        "description",
        "avatar",
        "banner",
        "visible_modules",
        "hidden_modules",
        "created_at",
        "modified_at",
        "user_count",
        "link_count",
        "team_links",
        "user_team_permissions",
    }
    ID: ClassVar["TeamsField"]
    NAME: ClassVar["TeamsField"]
    HANDLE: ClassVar["TeamsField"]
    SUMMARY: ClassVar["TeamsField"]
    DESCRIPTION: ClassVar["TeamsField"]
    AVATAR: ClassVar["TeamsField"]
    BANNER: ClassVar["TeamsField"]
    VISIBLE_MODULES: ClassVar["TeamsField"]
    HIDDEN_MODULES: ClassVar["TeamsField"]
    CREATED_AT: ClassVar["TeamsField"]
    MODIFIED_AT: ClassVar["TeamsField"]
    USER_COUNT: ClassVar["TeamsField"]
    LINK_COUNT: ClassVar["TeamsField"]
    TEAM_LINKS: ClassVar["TeamsField"]
    USER_TEAM_PERMISSIONS: ClassVar["TeamsField"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamsField.ID = TeamsField("id")
TeamsField.NAME = TeamsField("name")
TeamsField.HANDLE = TeamsField("handle")
TeamsField.SUMMARY = TeamsField("summary")
TeamsField.DESCRIPTION = TeamsField("description")
TeamsField.AVATAR = TeamsField("avatar")
TeamsField.BANNER = TeamsField("banner")
TeamsField.VISIBLE_MODULES = TeamsField("visible_modules")
TeamsField.HIDDEN_MODULES = TeamsField("hidden_modules")
TeamsField.CREATED_AT = TeamsField("created_at")
TeamsField.MODIFIED_AT = TeamsField("modified_at")
TeamsField.USER_COUNT = TeamsField("user_count")
TeamsField.LINK_COUNT = TeamsField("link_count")
TeamsField.TEAM_LINKS = TeamsField("team_links")
TeamsField.USER_TEAM_PERMISSIONS = TeamsField("user_team_permissions")
