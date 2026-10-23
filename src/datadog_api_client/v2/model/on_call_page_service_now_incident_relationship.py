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
    from datadog_api_client.v2.model.on_call_page_service_now_incident_relationship_data import (
        OnCallPageServiceNowIncidentRelationshipData,
    )


class OnCallPageServiceNowIncidentRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_service_now_incident_relationship_data import (
            OnCallPageServiceNowIncidentRelationshipData,
        )

        return {
            "data": (OnCallPageServiceNowIncidentRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[OnCallPageServiceNowIncidentRelationshipData, UnsetType] = unset, **kwargs):
        """
        The ServiceNow incident linked to the page.

        :param data: Reference to a ServiceNow incident.
        :type data: OnCallPageServiceNowIncidentRelationshipData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
