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
    from datadog_api_client.v2.model.vulnerability_severity import VulnerabilitySeverity


class EPSS(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.vulnerability_severity import VulnerabilitySeverity

        return {
            "score": (float,),
            "severity": (VulnerabilitySeverity,),
        }

    attribute_map = {
        "score": "score",
        "severity": "severity",
    }

    def __init__(self_, score: float, severity: VulnerabilitySeverity, **kwargs):
        """
        Vulnerability EPSS severity.

        :param score: Vulnerability EPSS severity score.
        :type score: float

        :param severity: The vulnerability severity.
        :type severity: VulnerabilitySeverity
        """
        super().__init__(kwargs)

        self_.score = score
        self_.severity = severity
