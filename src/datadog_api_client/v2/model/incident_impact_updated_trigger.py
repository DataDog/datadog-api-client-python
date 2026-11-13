# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.execution_limit import ExecutionLimit
    from datadog_api_client.v2.model.incident_trigger_incident_type import IncidentTriggerIncidentType
    from datadog_api_client.v2.model.incident_condition import IncidentCondition


class IncidentImpactUpdatedTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_limit import ExecutionLimit
        from datadog_api_client.v2.model.incident_trigger_incident_type import IncidentTriggerIncidentType
        from datadog_api_client.v2.model.incident_condition import IncidentCondition

        return {
            "execution_limit": (ExecutionLimit,),
            "incident_type": (str,),
            "incident_types": ([IncidentTriggerIncidentType],),
            "tag_condition": (IncidentCondition,),
        }

    attribute_map = {
        "execution_limit": "executionLimit",
        "incident_type": "incidentType",
        "incident_types": "incidentTypes",
        "tag_condition": "tagCondition",
    }

    def __init__(
        self_,
        execution_limit: Union[ExecutionLimit, UnsetType] = unset,
        incident_type: Union[str, UnsetType] = unset,
        incident_types: Union[List[IncidentTriggerIncidentType], UnsetType] = unset,
        tag_condition: Union[IncidentCondition, UnsetType] = unset,
        **kwargs,
    ):
        """
        Trigger a workflow when an impact is updated for an incident.

        :param execution_limit: The maximum number of times to execute a workflow for an incident.
        :type execution_limit: ExecutionLimit, optional

        :param incident_type: Deprecated. Use ``incidentTypes`` instead. The type of incident that triggers the workflow. **Deprecated**.
        :type incident_type: str, optional

        :param incident_types: The types of incident that trigger the workflow.
        :type incident_types: [IncidentTriggerIncidentType], optional

        :param tag_condition: Conditions that determine which incidents trigger the workflow.
        :type tag_condition: IncidentCondition, optional
        """
        if execution_limit is not unset:
            kwargs["execution_limit"] = execution_limit
        if incident_type is not unset:
            kwargs["incident_type"] = incident_type
        if incident_types is not unset:
            kwargs["incident_types"] = incident_types
        if tag_condition is not unset:
            kwargs["tag_condition"] = tag_condition
        super().__init__(kwargs)
