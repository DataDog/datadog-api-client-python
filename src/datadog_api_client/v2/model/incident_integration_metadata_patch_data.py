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


from datadog_api_client.v2.model.incident_integration_metadata_metadata import IncidentIntegrationMetadataMetadata
from datadog_api_client.v2.model.incident_integration_metadata_attributes import IncidentIntegrationMetadataAttributes
from datadog_api_client.v2.model.incident_integration_metadata_metadata import IncidentIntegrationMetadataMetadata
from datadog_api_client.v2.model.slack_integration_metadata import SlackIntegrationMetadata
from datadog_api_client.v2.model.jira_integration_metadata import JiraIntegrationMetadata

if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_integration_metadata_type import IncidentIntegrationMetadataType


@dataclass
class IncidentIntegrationMetadataPatchDataJSON:
    incident_id: Union[str, UnsetType] = unset
    integration_type: Union[int, UnsetType] = unset
    metadata: Union[
        IncidentIntegrationMetadataMetadata, SlackIntegrationMetadata, JiraIntegrationMetadata, UnsetType
    ] = unset
    status: Union[int, UnsetType] = unset


class IncidentIntegrationMetadataPatchData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_integration_metadata_type import IncidentIntegrationMetadataType

        return {
            "attributes": (IncidentIntegrationMetadataAttributes,),
            "type": (IncidentIntegrationMetadataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = IncidentIntegrationMetadataPatchDataJSON

    def __init__(
        self_, attributes: IncidentIntegrationMetadataAttributes, type: IncidentIntegrationMetadataType, **kwargs
    ):
        """
        Incident integration metadata data for a patch request.

        :param attributes: Incident integration metadata's attributes for a create request.
        :type attributes: IncidentIntegrationMetadataAttributes

        :param type: Integration metadata resource type.
        :type type: IncidentIntegrationMetadataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
