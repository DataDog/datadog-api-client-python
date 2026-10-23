# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgConnectionTypeEnum(ModelSimple):
    """
    Available connection types between organizations.

    :param value: Must be one of ["logs", "metrics", "audit", "ci_pipelines", "ci_tests"].
    :type value: str
    """

    allowed_values = {
        "logs",
        "metrics",
        "audit",
        "ci_pipelines",
        "ci_tests",
    }
    LOGS: ClassVar["OrgConnectionTypeEnum"]
    METRICS: ClassVar["OrgConnectionTypeEnum"]
    AUDIT: ClassVar["OrgConnectionTypeEnum"]
    CI_PIPELINES: ClassVar["OrgConnectionTypeEnum"]
    CI_TESTS: ClassVar["OrgConnectionTypeEnum"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgConnectionTypeEnum.LOGS = OrgConnectionTypeEnum("logs")
OrgConnectionTypeEnum.METRICS = OrgConnectionTypeEnum("metrics")
OrgConnectionTypeEnum.AUDIT = OrgConnectionTypeEnum("audit")
OrgConnectionTypeEnum.CI_PIPELINES = OrgConnectionTypeEnum("ci_pipelines")
OrgConnectionTypeEnum.CI_TESTS = OrgConnectionTypeEnum("ci_tests")
