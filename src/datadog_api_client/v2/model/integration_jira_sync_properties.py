# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sync_property import SyncProperty
    from datadog_api_client.v2.model.integration_jira_sync_properties_custom_fields_additional_properties import (
        IntegrationJiraSyncPropertiesCustomFieldsAdditionalProperties,
    )
    from datadog_api_client.v2.model.integration_jira_sync_due_date import IntegrationJiraSyncDueDate
    from datadog_api_client.v2.model.sync_property_with_mapping import SyncPropertyWithMapping


class IntegrationJiraSyncProperties(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sync_property import SyncProperty
        from datadog_api_client.v2.model.integration_jira_sync_properties_custom_fields_additional_properties import (
            IntegrationJiraSyncPropertiesCustomFieldsAdditionalProperties,
        )
        from datadog_api_client.v2.model.integration_jira_sync_due_date import IntegrationJiraSyncDueDate
        from datadog_api_client.v2.model.sync_property_with_mapping import SyncPropertyWithMapping

        return {
            "assignee": (SyncProperty,),
            "comments": (SyncProperty,),
            "custom_fields": ({str: (IntegrationJiraSyncPropertiesCustomFieldsAdditionalProperties,)},),
            "description": (SyncProperty,),
            "due_date": (IntegrationJiraSyncDueDate,),
            "priority": (SyncPropertyWithMapping,),
            "status": (SyncPropertyWithMapping,),
            "title": (SyncProperty,),
        }

    attribute_map = {
        "assignee": "assignee",
        "comments": "comments",
        "custom_fields": "custom_fields",
        "description": "description",
        "due_date": "due_date",
        "priority": "priority",
        "status": "status",
        "title": "title",
    }

    def __init__(
        self_,
        assignee: Union[SyncProperty, UnsetType] = unset,
        comments: Union[SyncProperty, UnsetType] = unset,
        custom_fields: Union[
            Dict[str, IntegrationJiraSyncPropertiesCustomFieldsAdditionalProperties], UnsetType
        ] = unset,
        description: Union[SyncProperty, UnsetType] = unset,
        due_date: Union[IntegrationJiraSyncDueDate, UnsetType] = unset,
        priority: Union[SyncPropertyWithMapping, UnsetType] = unset,
        status: Union[SyncPropertyWithMapping, UnsetType] = unset,
        title: Union[SyncProperty, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param assignee: Sync property configuration
        :type assignee: SyncProperty, optional

        :param comments: Sync property configuration
        :type comments: SyncProperty, optional

        :param custom_fields:
        :type custom_fields: {str: (IntegrationJiraSyncPropertiesCustomFieldsAdditionalProperties,)}, optional

        :param description: Sync property configuration
        :type description: SyncProperty, optional

        :param due_date:
        :type due_date: IntegrationJiraSyncDueDate, optional

        :param priority: Sync property with mapping configuration
        :type priority: SyncPropertyWithMapping, optional

        :param status: Sync property with mapping configuration
        :type status: SyncPropertyWithMapping, optional

        :param title: Sync property configuration
        :type title: SyncProperty, optional
        """
        if assignee is not unset:
            kwargs["assignee"] = assignee
        if comments is not unset:
            kwargs["comments"] = comments
        if custom_fields is not unset:
            kwargs["custom_fields"] = custom_fields
        if description is not unset:
            kwargs["description"] = description
        if due_date is not unset:
            kwargs["due_date"] = due_date
        if priority is not unset:
            kwargs["priority"] = priority
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
