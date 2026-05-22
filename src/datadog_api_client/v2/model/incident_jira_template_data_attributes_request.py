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


class IncidentJiraTemplateDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_jira_template_field_configuration import (
            IncidentJiraTemplateFieldConfiguration,
        )

        return {
            "account_id": (str,),
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
            "name": (str,),
            "project_id": (str,),
            "project_key": (str,),
            "sync_enabled": (bool,),
            "type": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "field_configurations": "field_configurations",
        "fields": "fields",
        "is_default": "is_default",
        "issue_id": "issue_id",
        "mappings": "mappings",
        "meta": "meta",
        "name": "name",
        "project_id": "project_id",
        "project_key": "project_key",
        "sync_enabled": "sync_enabled",
        "type": "type",
    }

    def __init__(
        self_,
        account_id: str,
        issue_id: str,
        project_id: str,
        project_key: str,
        field_configurations: Union[List[IncidentJiraTemplateFieldConfiguration], UnsetType] = unset,
        fields: Union[Dict[str, Any], UnsetType] = unset,
        is_default: Union[bool, UnsetType] = unset,
        mappings: Union[Dict[str, Any], UnsetType] = unset,
        meta: Union[Dict[str, Any], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        sync_enabled: Union[bool, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating an incident Jira template.

        :param account_id: The Jira account identifier.
        :type account_id: str

        :param field_configurations: Field configuration mappings.
        :type field_configurations: [IncidentJiraTemplateFieldConfiguration], optional

        :param fields: The Jira fields configuration.
        :type fields: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param is_default: Whether this is the default template.
        :type is_default: bool, optional

        :param issue_id: The Jira issue type identifier.
        :type issue_id: str

        :param mappings: The field mappings configuration.
        :type mappings: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param meta: Additional metadata for the template.
        :type meta: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param name: The name of the template.
        :type name: str, optional

        :param project_id: The Jira project identifier.
        :type project_id: str

        :param project_key: The Jira project key.
        :type project_key: str

        :param sync_enabled: Whether synchronization is enabled.
        :type sync_enabled: bool, optional

        :param type: The type of the template.
        :type type: str, optional
        """
        if field_configurations is not unset:
            kwargs["field_configurations"] = field_configurations
        if fields is not unset:
            kwargs["fields"] = fields
        if is_default is not unset:
            kwargs["is_default"] = is_default
        if mappings is not unset:
            kwargs["mappings"] = mappings
        if meta is not unset:
            kwargs["meta"] = meta
        if name is not unset:
            kwargs["name"] = name
        if sync_enabled is not unset:
            kwargs["sync_enabled"] = sync_enabled
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.issue_id = issue_id
        self_.project_id = project_id
        self_.project_key = project_key
