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
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_step_output import (
        SecurityMonitoringSignalInvestigationStepOutput,
    )


class SecurityMonitoringSignalInvestigationStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_step_output import (
            SecurityMonitoringSignalInvestigationStepOutput,
        )

        return {
            "step_outputs": ([SecurityMonitoringSignalInvestigationStepOutput],),
        }

    attribute_map = {
        "step_outputs": "stepOutputs",
    }

    def __init__(self_, step_outputs: List[SecurityMonitoringSignalInvestigationStepOutput], **kwargs):
        """
        Information about an investigation step.

        :param step_outputs: Array of step outputs.
        :type step_outputs: [SecurityMonitoringSignalInvestigationStepOutput]
        """
        super().__init__(kwargs)

        self_.step_outputs = step_outputs
