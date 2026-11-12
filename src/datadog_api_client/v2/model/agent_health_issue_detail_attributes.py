# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.agent_health_remediation import AgentHealthRemediation


class AgentHealthIssueDetailAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.agent_health_remediation import AgentHealthRemediation

        return {
            "category": (str,),
            "description": (str,),
            "first_seen_at": (datetime,),
            "issue_name": (str,),
            "issue_type": (str,),
            "remediation": (AgentHealthRemediation,),
            "resource_id": (str,),
            "resource_kind": (str,),
            "resource_type": (str,),
            "severity": (str,),
            "state": (str,),
            "tags": ([str],),
            "title": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "category": "category",
        "description": "description",
        "first_seen_at": "first_seen_at",
        "issue_name": "issue_name",
        "issue_type": "issue_type",
        "remediation": "remediation",
        "resource_id": "resource_id",
        "resource_kind": "resource_kind",
        "resource_type": "resource_type",
        "severity": "severity",
        "state": "state",
        "tags": "tags",
        "title": "title",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        issue_name: str,
        issue_type: str,
        resource_id: str,
        resource_kind: str,
        severity: str,
        state: str,
        category: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        first_seen_at: Union[datetime, UnsetType] = unset,
        remediation: Union[AgentHealthRemediation, UnsetType] = unset,
        resource_type: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an open Agent Health issue, including available remediation.

        :param category: The category of the issue, such as ``configuration``. Omitted when not set.
        :type category: str, optional

        :param description: The description of the issue. Omitted when empty.
        :type description: str, optional

        :param first_seen_at: The time the issue was first seen, in RFC 3339 format. Omitted when empty.
        :type first_seen_at: datetime, optional

        :param issue_name: The human-readable name of the issue.
        :type issue_name: str

        :param issue_type: The machine-readable type of the issue.
        :type issue_type: str

        :param remediation: Remediation for the issue. Omitted when no remediation is available.
        :type remediation: AgentHealthRemediation, optional

        :param resource_id: The identifier of the affected resource, interpreted according to ``resource_kind`` : hostname for ``host`` , DaemonSet UID for ``deployment`` (node Agent), cluster UUID for ``cluster`` , hostname of the host running the Cluster Agent for ``cluster_agent`` , or OpenTelemetry collector ID for ``otel``.
        :type resource_id: str

        :param resource_kind: The kind of affected resource. Known values are ``host`` , ``deployment`` , ``cluster`` , ``cluster_agent`` , and ``otel``.
        :type resource_kind: str

        :param resource_type: The type of the affected resource. Omitted when empty.
        :type resource_type: str, optional

        :param severity: The severity of the issue. Known values are ``low`` , ``medium`` , ``high`` , and ``unknown``.
        :type severity: str

        :param state: The state of the issue. Only issues with state ``open`` are returned.
        :type state: str

        :param tags: Tags associated with the issue. Omitted when empty.
        :type tags: [str], optional

        :param title: The title of the issue. Omitted when empty.
        :type title: str, optional

        :param updated_at: The time the issue was last updated, in RFC 3339 format. Omitted when empty.
        :type updated_at: datetime, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if description is not unset:
            kwargs["description"] = description
        if first_seen_at is not unset:
            kwargs["first_seen_at"] = first_seen_at
        if remediation is not unset:
            kwargs["remediation"] = remediation
        if resource_type is not unset:
            kwargs["resource_type"] = resource_type
        if tags is not unset:
            kwargs["tags"] = tags
        if title is not unset:
            kwargs["title"] = title
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.issue_name = issue_name
        self_.issue_type = issue_type
        self_.resource_id = resource_id
        self_.resource_kind = resource_kind
        self_.severity = severity
        self_.state = state
