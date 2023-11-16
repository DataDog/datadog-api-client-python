# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_integration_metadata_metadata import IncidentIntegrationMetadataMetadata
    from datadog_api_client.v2.model.slack_integration_metadata import SlackIntegrationMetadata
    from datadog_api_client.v2.model.jira_integration_metadata import JiraIntegrationMetadata


class IncidentIntegrationMetadataAttributes(ModelNormal):
    validations = {
        "integration_type": {
            "inclusive_maximum": 9,
        },
        "status": {
            "inclusive_maximum": 5,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_integration_metadata_metadata import (
            IncidentIntegrationMetadataMetadata,
        )

        return {
            "created": (datetime,),
            "incident_id": (str,),
            "integration_type": (int,),
            "metadata": (IncidentIntegrationMetadataMetadata,),
            "modified": (datetime,),
            "status": (int,),
        }

    attribute_map = {
        "created": "created",
        "incident_id": "incident_id",
        "integration_type": "integration_type",
        "metadata": "metadata",
        "modified": "modified",
        "status": "status",
    }
    read_only_vars = {
        "created",
        "modified",
    }

    def __init__(
        self_,
        integration_type: int,
        metadata: Union[IncidentIntegrationMetadataMetadata, SlackIntegrationMetadata, JiraIntegrationMetadata],
        created: Union[datetime, UnsetType] = unset,
        incident_id: Union[str, UnsetType] = unset,
        modified: Union[datetime, UnsetType] = unset,
        status: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident integration metadata's attributes for a create request.

        :param created: Timestamp when the incident todo was created.
        :type created: datetime, optional

        :param incident_id: UUID of the incident this integration metadata is connected to.
        :type incident_id: str, optional

        :param integration_type: A number indicating the type of integration this metadata is for. 1 indicates Slack;
            8 indicates Jira.
        :type integration_type: int

        :param metadata: Incident integration metadata's metadata attribute.
        :type metadata: IncidentIntegrationMetadataMetadata

        :param modified: Timestamp when the incident todo was last modified.
        :type modified: datetime, optional

        :param status: A number indicating the status of this integration metadata. 0 indicates unknown;
            1 indicates pending; 2 indicates complete; 3 indicates manually created;
            4 indicates manually updated; 5 indicates failed.
        :type status: int, optional
        """
        if created is not unset:
            kwargs["created"] = created
        if incident_id is not unset:
            kwargs["incident_id"] = incident_id
        if modified is not unset:
            kwargs["modified"] = modified
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)

        self_.integration_type = integration_type
        self_.metadata = metadata
