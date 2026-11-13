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
    from datadog_api_client.v2.model.issue_impact_view_counts import IssueImpactViewCounts
    from datadog_api_client.v2.model.issue_impact_error_counts import IssueImpactErrorCounts


class IssueImpactView(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_impact_view_counts import IssueImpactViewCounts
        from datadog_api_client.v2.model.issue_impact_error_counts import IssueImpactErrorCounts

        return {
            "affected": (IssueImpactViewCounts,),
            "baseline": (IssueImpactViewCounts,),
            "error_counts": (IssueImpactErrorCounts,),
            "name": (str,),
            "significant": (bool,),
        }

    attribute_map = {
        "affected": "affected",
        "baseline": "baseline",
        "error_counts": "error_counts",
        "name": "name",
        "significant": "significant",
    }

    def __init__(
        self_,
        affected: IssueImpactViewCounts,
        error_counts: IssueImpactErrorCounts,
        name: str,
        significant: bool,
        baseline: Union[IssueImpactViewCounts, UnsetType] = unset,
        **kwargs,
    ):
        """
        A RUM view where the issue occurred.

        :param affected: Distinct users, accounts, sessions, and view instances on a view. ``affected`` counts only those with the issue's
            errors. ``baseline`` counts all users, accounts, sessions, and view instances on the view in the time window. It
            is absent when RUM has no data for the view.
        :type affected: IssueImpactViewCounts

        :param baseline: Distinct users, accounts, sessions, and view instances on a view. ``affected`` counts only those with the issue's
            errors. ``baseline`` counts all users, accounts, sessions, and view instances on the view in the time window. It
            is absent when RUM has no data for the view.
        :type baseline: IssueImpactViewCounts, optional

        :param error_counts: Number of errors reported by each source. Several sources can report the same error, such as an APM span and
            a log, so the counts overlap: don't add them together.
        :type error_counts: IssueImpactErrorCounts

        :param name: View name.
        :type name: str

        :param significant: Whether the entry stands out as a likely driver of the issue, because it accounts for most of the issue's
            errors or for far more errors than the other listed entries.
        :type significant: bool
        """
        if baseline is not unset:
            kwargs["baseline"] = baseline
        super().__init__(kwargs)

        self_.affected = affected
        self_.error_counts = error_counts
        self_.name = name
        self_.significant = significant
