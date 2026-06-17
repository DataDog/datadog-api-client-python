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
    from datadog_api_client.v2.model.governance_insight_audit_compute import GovernanceInsightAuditCompute


class GovernanceInsightAuditQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_insight_audit_compute import GovernanceInsightAuditCompute

        return {
            "compute": (GovernanceInsightAuditCompute,),
            "indexes": ([str],),
            "query": (str,),
            "source": (str,),
        }

    attribute_map = {
        "compute": "compute",
        "indexes": "indexes",
        "query": "query",
        "source": "source",
    }

    def __init__(self_, compute: GovernanceInsightAuditCompute, indexes: List[str], query: str, source: str, **kwargs):
        """
        An audit log query used to compute an insight value.

        :param compute: The aggregation applied to an audit log query.
        :type compute: GovernanceInsightAuditCompute

        :param indexes: The audit log indexes the query runs against.
        :type indexes: [str]

        :param query: The audit log search query string.
        :type query: str

        :param source: The data source the query runs against.
        :type source: str
        """
        super().__init__(kwargs)

        self_.compute = compute
        self_.indexes = indexes
        self_.query = query
        self_.source = source
