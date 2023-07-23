# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_integration_metadata_create_data import (
        IncidentIntegrationMetadataCreateData,
    )
    from datadog_api_client.v2.model.incident_integration_metadata_metadata import IncidentIntegrationMetadataMetadata
    from datadog_api_client.v2.model.slack_integration_metadata import SlackIntegrationMetadata
    from datadog_api_client.v2.model.jira_integration_metadata import JiraIntegrationMetadata


@dataclass
class IncidentIntegrationMetadataCreateRequestJSON:
    incident_id: Union[str, UnsetType] = unset
    integration_type: Union[int, UnsetType] = unset
    metadata: Union[
        IncidentIntegrationMetadataMetadata, SlackIntegrationMetadata, JiraIntegrationMetadata, UnsetType
    ] = unset
    status: Union[int, UnsetType] = unset


class IncidentIntegrationMetadataCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_integration_metadata_create_data import (
            IncidentIntegrationMetadataCreateData,
        )

        return {
            "data": (IncidentIntegrationMetadataCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = IncidentIntegrationMetadataCreateRequestJSON

    def __init__(self_, data: IncidentIntegrationMetadataCreateData, **kwargs):
        """
        Create request for an incident integration metadata.

        :param data: Incident integration metadata data for a create request.
        :type data: IncidentIntegrationMetadataCreateData
        """
        super().__init__(kwargs)

        self_.data = data
