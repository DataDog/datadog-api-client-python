# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CaseBulkActionType(ModelSimple):
    """
    The type of action to apply in a bulk update. Allowed values are `priority`, `status`, `assign`, `unassign`, `archive`, `unarchive`, `jira`, `servicenow`, `linear`, `update_project`.

    :param value: Must be one of ["priority", "status", "assign", "unassign", "archive", "unarchive", "jira", "servicenow", "linear", "update_project"].
    :type value: str
    """

    allowed_values = {
        "priority",
        "status",
        "assign",
        "unassign",
        "archive",
        "unarchive",
        "jira",
        "servicenow",
        "linear",
        "update_project",
    }
    PRIORITY: ClassVar["CaseBulkActionType"]
    STATUS: ClassVar["CaseBulkActionType"]
    ASSIGN: ClassVar["CaseBulkActionType"]
    UNASSIGN: ClassVar["CaseBulkActionType"]
    ARCHIVE: ClassVar["CaseBulkActionType"]
    UNARCHIVE: ClassVar["CaseBulkActionType"]
    JIRA: ClassVar["CaseBulkActionType"]
    SERVICENOW: ClassVar["CaseBulkActionType"]
    LINEAR: ClassVar["CaseBulkActionType"]
    UPDATE_PROJECT: ClassVar["CaseBulkActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CaseBulkActionType.PRIORITY = CaseBulkActionType("priority")
CaseBulkActionType.STATUS = CaseBulkActionType("status")
CaseBulkActionType.ASSIGN = CaseBulkActionType("assign")
CaseBulkActionType.UNASSIGN = CaseBulkActionType("unassign")
CaseBulkActionType.ARCHIVE = CaseBulkActionType("archive")
CaseBulkActionType.UNARCHIVE = CaseBulkActionType("unarchive")
CaseBulkActionType.JIRA = CaseBulkActionType("jira")
CaseBulkActionType.SERVICENOW = CaseBulkActionType("servicenow")
CaseBulkActionType.LINEAR = CaseBulkActionType("linear")
CaseBulkActionType.UPDATE_PROJECT = CaseBulkActionType("update_project")
