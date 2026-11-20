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
    from datadog_api_client.v2.model.remediation_group_findings_by_severity import RemediationGroupFindingsBySeverity


class RemediationGroupFindings(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_group_findings_by_severity import (
            RemediationGroupFindingsBySeverity,
        )

        return {
            "by_severity": (RemediationGroupFindingsBySeverity,),
            "total": (int,),
        }

    attribute_map = {
        "by_severity": "by_severity",
        "total": "total",
    }

    def __init__(self_, by_severity: RemediationGroupFindingsBySeverity, total: int, **kwargs):
        """
        Counts of the group's open findings. The counts include every finding in the group, including findings that
        don't match ``filter[query]``.

        :param by_severity: Number of the group's findings for each value of their ``@severity`` attribute. The response includes every
            level, including levels with a count of zero.
        :type by_severity: RemediationGroupFindingsBySeverity

        :param total: Number of open findings in the group.
        :type total: int
        """
        super().__init__(kwargs)

        self_.by_severity = by_severity
        self_.total = total
