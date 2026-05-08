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
    from datadog_api_client.v2.model.replay_analysis_affected_session import ReplayAnalysisAffectedSession
    from datadog_api_client.v2.model.replay_analysis_representative_session import ReplayAnalysisRepresentativeSession


class ReplayAnalysisIssueDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.replay_analysis_affected_session import ReplayAnalysisAffectedSession
        from datadog_api_client.v2.model.replay_analysis_representative_session import (
            ReplayAnalysisRepresentativeSession,
        )

        return {
            "affected_sessions": ([ReplayAnalysisAffectedSession],),
            "application_id": (str,),
            "created_at": (datetime,),
            "description": (str,),
            "journey_query": (
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
                none_type,
            ),
            "name": (str,),
            "representative_session": (ReplayAnalysisRepresentativeSession,),
            "session_count": (int,),
            "severity": (str,),
            "updated_at": (datetime,),
            "validation_verdict": (str,),
        }

    attribute_map = {
        "affected_sessions": "affected_sessions",
        "application_id": "application_id",
        "created_at": "created_at",
        "description": "description",
        "journey_query": "journey_query",
        "name": "name",
        "representative_session": "representative_session",
        "session_count": "session_count",
        "severity": "severity",
        "updated_at": "updated_at",
        "validation_verdict": "validation_verdict",
    }

    def __init__(
        self_,
        affected_sessions: List[ReplayAnalysisAffectedSession],
        application_id: str,
        created_at: datetime,
        description: str,
        name: str,
        representative_session: ReplayAnalysisRepresentativeSession,
        session_count: int,
        severity: str,
        updated_at: datetime,
        validation_verdict: str,
        journey_query: Union[Dict[str, Any], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a RUM replay analysis issue.

        :param affected_sessions: Up to three sample sessions affected by this issue.
        :type affected_sessions: [ReplayAnalysisAffectedSession]

        :param application_id: Unique identifier of the application where the issue was detected.
        :type application_id: str

        :param created_at: Timestamp when the issue was first detected.
        :type created_at: datetime

        :param description: Human-readable description of the issue.
        :type description: str

        :param journey_query: Journey query associated with the issue.
        :type journey_query: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param name: Name of the issue.
        :type name: str

        :param representative_session: A representative session illustrating a replay analysis issue.
        :type representative_session: ReplayAnalysisRepresentativeSession

        :param session_count: Total number of sessions affected by this issue.
        :type session_count: int

        :param severity: Severity level of the issue. Valid values are ``high`` , ``medium`` , and ``low``.
        :type severity: str

        :param updated_at: Timestamp when the issue was last updated.
        :type updated_at: datetime

        :param validation_verdict: Validation status of the issue.
        :type validation_verdict: str
        """
        if journey_query is not unset:
            kwargs["journey_query"] = journey_query
        super().__init__(kwargs)

        self_.affected_sessions = affected_sessions
        self_.application_id = application_id
        self_.created_at = created_at
        self_.description = description
        self_.name = name
        self_.representative_session = representative_session
        self_.session_count = session_count
        self_.severity = severity
        self_.updated_at = updated_at
        self_.validation_verdict = validation_verdict
