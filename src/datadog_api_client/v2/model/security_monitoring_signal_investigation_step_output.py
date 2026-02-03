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
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_step_output_verdict import (
        SecurityMonitoringSignalInvestigationStepOutputVerdict,
    )


class SecurityMonitoringSignalInvestigationStepOutput(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_step_output_verdict import (
            SecurityMonitoringSignalInvestigationStepOutputVerdict,
        )

        return {
            "current_step_analysis_oneliner": (str,),
            "current_step_analysis_summary": (str,),
            "name": (str,),
            "verdict": (SecurityMonitoringSignalInvestigationStepOutputVerdict,),
        }

    attribute_map = {
        "current_step_analysis_oneliner": "currentStepAnalysisOneliner",
        "current_step_analysis_summary": "currentStepAnalysisSummary",
        "name": "name",
        "verdict": "verdict",
    }

    def __init__(
        self_,
        current_step_analysis_summary: str,
        name: str,
        verdict: SecurityMonitoringSignalInvestigationStepOutputVerdict,
        current_step_analysis_oneliner: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Output from an investigation step.

        :param current_step_analysis_oneliner: A one-line summary of the step analysis.
        :type current_step_analysis_oneliner: str, optional

        :param current_step_analysis_summary: A detailed summary of the step analysis.
        :type current_step_analysis_summary: str

        :param name: The name of the investigation step.
        :type name: str

        :param verdict: The verdict from the investigation step.
        :type verdict: SecurityMonitoringSignalInvestigationStepOutputVerdict
        """
        if current_step_analysis_oneliner is not unset:
            kwargs["current_step_analysis_oneliner"] = current_step_analysis_oneliner
        super().__init__(kwargs)

        self_.current_step_analysis_summary = current_step_analysis_summary
        self_.name = name
        self_.verdict = verdict
