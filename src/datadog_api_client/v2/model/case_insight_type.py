# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CaseInsightType(ModelSimple):
    """
    The type of Datadog resource linked to the case as contextual evidence. Each type corresponds to a different Datadog product signal (for example, a security finding, a monitor alert, or an incident).

    :param value: Must be one of ["SECURITY_SIGNAL", "MONITOR", "EVENT_CORRELATION", "ERROR_TRACKING", "CLOUD_COST_RECOMMENDATION", "INCIDENT", "SENSITIVE_DATA_SCANNER_ISSUE", "EVENT", "WATCHDOG_STORY", "WIDGET", "SECURITY_FINDING", "INSIGHT_SCORECARD_CAMPAIGN", "RESOURCE_POLICY", "APM_RECOMMENDATION", "SCM_URL", "PROFILING_DOWNSIZING_EXPERIMENT"].
    :type value: str
    """

    allowed_values = {
        "SECURITY_SIGNAL",
        "MONITOR",
        "EVENT_CORRELATION",
        "ERROR_TRACKING",
        "CLOUD_COST_RECOMMENDATION",
        "INCIDENT",
        "SENSITIVE_DATA_SCANNER_ISSUE",
        "EVENT",
        "WATCHDOG_STORY",
        "WIDGET",
        "SECURITY_FINDING",
        "INSIGHT_SCORECARD_CAMPAIGN",
        "RESOURCE_POLICY",
        "APM_RECOMMENDATION",
        "SCM_URL",
        "PROFILING_DOWNSIZING_EXPERIMENT",
    }
    SECURITY_SIGNAL: ClassVar["CaseInsightType"]
    MONITOR: ClassVar["CaseInsightType"]
    EVENT_CORRELATION: ClassVar["CaseInsightType"]
    ERROR_TRACKING: ClassVar["CaseInsightType"]
    CLOUD_COST_RECOMMENDATION: ClassVar["CaseInsightType"]
    INCIDENT: ClassVar["CaseInsightType"]
    SENSITIVE_DATA_SCANNER_ISSUE: ClassVar["CaseInsightType"]
    EVENT: ClassVar["CaseInsightType"]
    WATCHDOG_STORY: ClassVar["CaseInsightType"]
    WIDGET: ClassVar["CaseInsightType"]
    SECURITY_FINDING: ClassVar["CaseInsightType"]
    INSIGHT_SCORECARD_CAMPAIGN: ClassVar["CaseInsightType"]
    RESOURCE_POLICY: ClassVar["CaseInsightType"]
    APM_RECOMMENDATION: ClassVar["CaseInsightType"]
    SCM_URL: ClassVar["CaseInsightType"]
    PROFILING_DOWNSIZING_EXPERIMENT: ClassVar["CaseInsightType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CaseInsightType.SECURITY_SIGNAL = CaseInsightType("SECURITY_SIGNAL")
CaseInsightType.MONITOR = CaseInsightType("MONITOR")
CaseInsightType.EVENT_CORRELATION = CaseInsightType("EVENT_CORRELATION")
CaseInsightType.ERROR_TRACKING = CaseInsightType("ERROR_TRACKING")
CaseInsightType.CLOUD_COST_RECOMMENDATION = CaseInsightType("CLOUD_COST_RECOMMENDATION")
CaseInsightType.INCIDENT = CaseInsightType("INCIDENT")
CaseInsightType.SENSITIVE_DATA_SCANNER_ISSUE = CaseInsightType("SENSITIVE_DATA_SCANNER_ISSUE")
CaseInsightType.EVENT = CaseInsightType("EVENT")
CaseInsightType.WATCHDOG_STORY = CaseInsightType("WATCHDOG_STORY")
CaseInsightType.WIDGET = CaseInsightType("WIDGET")
CaseInsightType.SECURITY_FINDING = CaseInsightType("SECURITY_FINDING")
CaseInsightType.INSIGHT_SCORECARD_CAMPAIGN = CaseInsightType("INSIGHT_SCORECARD_CAMPAIGN")
CaseInsightType.RESOURCE_POLICY = CaseInsightType("RESOURCE_POLICY")
CaseInsightType.APM_RECOMMENDATION = CaseInsightType("APM_RECOMMENDATION")
CaseInsightType.SCM_URL = CaseInsightType("SCM_URL")
CaseInsightType.PROFILING_DOWNSIZING_EXPERIMENT = CaseInsightType("PROFILING_DOWNSIZING_EXPERIMENT")
