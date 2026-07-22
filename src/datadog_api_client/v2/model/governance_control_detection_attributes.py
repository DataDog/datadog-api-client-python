# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

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
    from datadog_api_client.v2.model.governance_control_detection_assignment_source import (
        GovernanceControlDetectionAssignmentSource,
    )
    from datadog_api_client.v2.model.governance_control_detection_state import GovernanceControlDetectionState


class GovernanceControlDetectionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_detection_assignment_source import (
            GovernanceControlDetectionAssignmentSource,
        )
        from datadog_api_client.v2.model.governance_control_detection_state import GovernanceControlDetectionState

        return {
            "assigned_team": (str,),
            "assigned_to": (str,),
            "assignment_source": (GovernanceControlDetectionAssignmentSource,),
            "control_id": (str,),
            "created_at": (datetime,),
            "detection_type": (str,),
            "display_name": (str,),
            "exception_at": (datetime,),
            "exception_by": (str,),
            "metadata": (
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
            ),
            "mitigate_after": (datetime,),
            "mitigated_at": (datetime,),
            "priority": (int,),
            "resource_id": (str,),
            "resource_url": (str,),
            "state": (GovernanceControlDetectionState,),
        }

    attribute_map = {
        "assigned_team": "assigned_team",
        "assigned_to": "assigned_to",
        "assignment_source": "assignment_source",
        "control_id": "control_id",
        "created_at": "created_at",
        "detection_type": "detection_type",
        "display_name": "display_name",
        "exception_at": "exception_at",
        "exception_by": "exception_by",
        "metadata": "metadata",
        "mitigate_after": "mitigate_after",
        "mitigated_at": "mitigated_at",
        "priority": "priority",
        "resource_id": "resource_id",
        "resource_url": "resource_url",
        "state": "state",
    }

    def __init__(
        self_,
        assignment_source: GovernanceControlDetectionAssignmentSource,
        control_id: str,
        created_at: datetime,
        detection_type: str,
        display_name: str,
        priority: int,
        resource_id: str,
        resource_url: str,
        state: GovernanceControlDetectionState,
        assigned_team: Union[str, UnsetType] = unset,
        assigned_to: Union[str, UnsetType] = unset,
        exception_at: Union[datetime, UnsetType] = unset,
        exception_by: Union[str, UnsetType] = unset,
        metadata: Union[Any, UnsetType] = unset,
        mitigate_after: Union[datetime, UnsetType] = unset,
        mitigated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a governance control detection.

        :param assigned_team: The identifier of the team the detection is assigned to, if any.
        :type assigned_team: str, optional

        :param assigned_to: The identifier of the user the detection is assigned to, if any.
        :type assigned_to: str, optional

        :param assignment_source: How the detection's current assignment was determined. Possible values are ``auto_resolved`` , ``manual`` , ``reassigned`` , and ``cleared``.
        :type assignment_source: GovernanceControlDetectionAssignmentSource

        :param control_id: The unique identifier of the control that produced this detection.
        :type control_id: str

        :param created_at: The date and time when the detection was created.
        :type created_at: datetime

        :param detection_type: The type of detection, which determines what condition was detected.
        :type detection_type: str

        :param display_name: The human-readable name of the detected resource.
        :type display_name: str

        :param exception_at: The date and time when the detection was marked as an exception, if applicable.
        :type exception_at: datetime, optional

        :param exception_by: The identifier of the user who marked the detection as an exception, if applicable.
        :type exception_by: str, optional

        :param metadata: Free-form metadata associated with the detection.
        :type metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param mitigate_after: The date and time after which the detection is scheduled to be mitigated, if applicable.
        :type mitigate_after: datetime, optional

        :param mitigated_at: The date and time when the detection was mitigated, if applicable.
        :type mitigated_at: datetime, optional

        :param priority: The priority of the detection, if set.
        :type priority: int

        :param resource_id: The identifier of the resource the detection applies to.
        :type resource_id: str

        :param resource_url: A link to the detected resource in Datadog.
        :type resource_url: str

        :param state: The current state of the detection. Possible values are ``active`` , ``exception`` , ``mitigated`` , ``inactive`` , ``obsolete`` , ``resolved_externally`` , and ``mitigation_in_progress``.
        :type state: GovernanceControlDetectionState
        """
        if assigned_team is not unset:
            kwargs["assigned_team"] = assigned_team
        if assigned_to is not unset:
            kwargs["assigned_to"] = assigned_to
        if exception_at is not unset:
            kwargs["exception_at"] = exception_at
        if exception_by is not unset:
            kwargs["exception_by"] = exception_by
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if mitigate_after is not unset:
            kwargs["mitigate_after"] = mitigate_after
        if mitigated_at is not unset:
            kwargs["mitigated_at"] = mitigated_at
        super().__init__(kwargs)

        self_.assignment_source = assignment_source
        self_.control_id = control_id
        self_.created_at = created_at
        self_.detection_type = detection_type
        self_.display_name = display_name
        self_.priority = priority
        self_.resource_id = resource_id
        self_.resource_url = resource_url
        self_.state = state
