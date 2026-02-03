# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_metric import (
        SecurityMonitoringSignalInvestigationFeedbackMetric,
    )


class SecurityMonitoringSignalInvestigationFeedbackSection(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_metric import (
            SecurityMonitoringSignalInvestigationFeedbackMetric,
        )

        return {
            "id": (str,),
            "metrics": ([SecurityMonitoringSignalInvestigationFeedbackMetric],),
            "title": (str,),
        }

    attribute_map = {
        "id": "id",
        "metrics": "metrics",
        "title": "title",
    }

    def __init__(
        self_, id: str, metrics: List[SecurityMonitoringSignalInvestigationFeedbackMetric], title: str, **kwargs
    ):
        """
        A feedback section containing metrics.

        :param id: The section identifier.
        :type id: str

        :param metrics: Array of feedback metrics.
        :type metrics: [SecurityMonitoringSignalInvestigationFeedbackMetric]

        :param title: The section title.
        :type title: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.metrics = metrics
        self_.title = title
