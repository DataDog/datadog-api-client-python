# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_jira_template_field_configuration import (
        IncidentJiraTemplateFieldConfiguration,
    )


class IncidentJiraTemplateDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_jira_template_field_configuration import (
            IncidentJiraTemplateFieldConfiguration,
        )

        return {
            "account_id": (str,),
            "created": (datetime,),
            "created_by_uuid": (UUID,),
            "field_configurations": ([IncidentJiraTemplateFieldConfiguration],),
            "fields": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "is_default": (bool,),
            "issue_id": (str,),
            "last_modified_by_uuid": (UUID,),
            "mappings": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "meta": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "modified": (datetime,),
            "name": (str,),
            "project_id": (str,),
            "project_key": (str,),
            "sync_enabled": (bool,),
            "type": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "created": "created",
        "created_by_uuid": "created_by_uuid",
        "field_configurations": "field_configurations",
        "fields": "fields",
        "is_default": "is_default",
        "issue_id": "issue_id",
        "last_modified_by_uuid": "last_modified_by_uuid",
        "mappings": "mappings",
        "meta": "meta",
        "modified": "modified",
        "name": "name",
        "project_id": "project_id",
        "project_key": "project_key",
        "sync_enabled": "sync_enabled",
        "type": "type",
    }

    def __init__(
        self_,
        account_id: str,
        created: datetime,
        created_by_uuid: UUID,
        is_default: bool,
        issue_id: str,
        last_modified_by_uuid: UUID,
        modified: datetime,
        name: str,
        project_id: str,
        project_key: str,
        sync_enabled: bool,
        type: str,
        field_configurations: Union[List[IncidentJiraTemplateFieldConfiguration], UnsetType] = unset,
        fields: Union[Dict[str, Any], UnsetType] = unset,
        mappings: Union[Dict[str, Any], UnsetType] = unset,
        meta: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an incident Jira template.

        :param account_id: The Jira account identifier.
        :type account_id: str

        :param created: Timestamp when the template was created.
        :type created: datetime

        :param created_by_uuid: UUID of the user who created the template.
        :type created_by_uuid: UUID

        :param field_configurations: Field configuration mappings.
        :type field_configurations: [IncidentJiraTemplateFieldConfiguration], optional

        :param fields: The Jira fields configuration.
        :type fields: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param is_default: Whether this is the default template.
        :type is_default: bool

        :param issue_id: The Jira issue type identifier.
        :type issue_id: str

        :param last_modified_by_uuid: UUID of the user who last modified the template.
        :type last_modified_by_uuid: UUID

        :param mappings: The field mappings configuration.
        :type mappings: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param meta: Additional metadata for the template.
        :type meta: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param modified: Timestamp when the template was last modified.
        :type modified: datetime

        :param name: The name of the template.
        :type name: str

        :param project_id: The Jira project identifier.
        :type project_id: str

        :param project_key: The Jira project key.
        :type project_key: str

        :param sync_enabled: Whether synchronization is enabled.
        :type sync_enabled: bool

        :param type: The type of the template.
        :type type: str
        """
        if field_configurations is not unset:
            kwargs["field_configurations"] = field_configurations
        if fields is not unset:
            kwargs["fields"] = fields
        if mappings is not unset:
            kwargs["mappings"] = mappings
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.created = created
        self_.created_by_uuid = created_by_uuid
        self_.is_default = is_default
        self_.issue_id = issue_id
        self_.last_modified_by_uuid = last_modified_by_uuid
        self_.modified = modified
        self_.name = name
        self_.project_id = project_id
        self_.project_key = project_key
        self_.sync_enabled = sync_enabled
        self_.type = type
