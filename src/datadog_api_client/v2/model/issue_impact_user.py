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
    from datadog_api_client.v2.model.issue_impact_error_counts import IssueImpactErrorCounts


class IssueImpactUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_impact_error_counts import IssueImpactErrorCounts

        return {
            "error_counts": (IssueImpactErrorCounts,),
            "id": (str,),
            "name": (str,),
            "significant": (bool,),
        }

    attribute_map = {
        "error_counts": "error_counts",
        "id": "id",
        "name": "name",
        "significant": "significant",
    }

    def __init__(
        self_,
        error_counts: IssueImpactErrorCounts,
        id: str,
        significant: bool,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A user affected by the issue.

        :param error_counts: Number of errors reported by each source. Several sources can report the same error, such as an APM span and
            a log, so the counts overlap: don't add them together.
        :type error_counts: IssueImpactErrorCounts

        :param id: User ID, from the ``usr.id`` attribute.
        :type id: str

        :param name: User name or email, if available.
        :type name: str, optional

        :param significant: Whether the entry stands out as a likely driver of the issue, because it accounts for most of the issue's
            errors or for far more errors than the other listed entries.
        :type significant: bool
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.error_counts = error_counts
        self_.id = id
        self_.significant = significant
