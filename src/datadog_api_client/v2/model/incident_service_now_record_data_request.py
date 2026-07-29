# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_service_now_record_data_attributes_request import (
        IncidentServiceNowRecordDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_service_now_record_prompt_type import IncidentServiceNowRecordPromptType


class IncidentServiceNowRecordDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_service_now_record_data_attributes_request import (
            IncidentServiceNowRecordDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_service_now_record_prompt_type import (
            IncidentServiceNowRecordPromptType,
        )

        return {
            "attributes": (IncidentServiceNowRecordDataAttributesRequest,),
            "type": (IncidentServiceNowRecordPromptType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentServiceNowRecordDataAttributesRequest,
        type: IncidentServiceNowRecordPromptType,
        **kwargs,
    ):
        """
        ServiceNow record data in a create request.

        :param attributes: Attributes for creating a ServiceNow record for an incident.
        :type attributes: IncidentServiceNowRecordDataAttributesRequest

        :param type: ServiceNow record prompt resource type.
        :type type: IncidentServiceNowRecordPromptType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
