# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.integration_jira_auto_creation import IntegrationJiraAutoCreation
    from datadog_api_client.v2.model.integration_jira_metadata import IntegrationJiraMetadata
    from datadog_api_client.v2.model.integration_jira_sync import IntegrationJiraSync


class IntegrationJira(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_jira_auto_creation import IntegrationJiraAutoCreation
        from datadog_api_client.v2.model.integration_jira_metadata import IntegrationJiraMetadata
        from datadog_api_client.v2.model.integration_jira_sync import IntegrationJiraSync

        return {
            "auto_creation": (IntegrationJiraAutoCreation,),
            "enabled": (bool,),
            "metadata": (IntegrationJiraMetadata,),
            "sync": (IntegrationJiraSync,),
        }

    attribute_map = {
        "auto_creation": "auto_creation",
        "enabled": "enabled",
        "metadata": "metadata",
        "sync": "sync",
    }

    def __init__(
        self_,
        auto_creation: Union[IntegrationJiraAutoCreation, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        metadata: Union[IntegrationJiraMetadata, UnsetType] = unset,
        sync: Union[IntegrationJiraSync, UnsetType] = unset,
        **kwargs,
    ):
        """
        Jira integration settings

        :param auto_creation:
        :type auto_creation: IntegrationJiraAutoCreation, optional

        :param enabled: Whether Jira integration is enabled
        :type enabled: bool, optional

        :param metadata:
        :type metadata: IntegrationJiraMetadata, optional

        :param sync:
        :type sync: IntegrationJiraSync, optional
        """
        if auto_creation is not unset:
            kwargs["auto_creation"] = auto_creation
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if sync is not unset:
            kwargs["sync"] = sync
        super().__init__(kwargs)
