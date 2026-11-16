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
    from datadog_api_client.v2.model.issue_impact_error_counts import IssueImpactErrorCounts


class IssueImpactEndpoint(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_impact_error_counts import IssueImpactErrorCounts

        return {
            "error_counts": (IssueImpactErrorCounts,),
            "resource_name": (str,),
            "service": (str,),
            "significant": (bool,),
        }

    attribute_map = {
        "error_counts": "error_counts",
        "resource_name": "resource_name",
        "service": "service",
        "significant": "significant",
    }

    def __init__(
        self_, error_counts: IssueImpactErrorCounts, resource_name: str, service: str, significant: bool, **kwargs
    ):
        """
        An endpoint whose traces have the issue's errors.

        :param error_counts: Number of errors reported by each source. Several sources can report the same error, such as an APM span and
            a log, so the counts overlap: don't add them together.
        :type error_counts: IssueImpactErrorCounts

        :param resource_name: Resource name of the trace's root span.
        :type resource_name: str

        :param service: Service of the trace's root span.
        :type service: str

        :param significant: Whether the entry stands out as a likely driver of the issue, because it accounts for most of the issue's
            errors or for far more errors than the other listed entries.
        :type significant: bool
        """
        super().__init__(kwargs)

        self_.error_counts = error_counts
        self_.resource_name = resource_name
        self_.service = service
        self_.significant = significant
