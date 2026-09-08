# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class UnitCostQuery(ModelNormal):
    def __init__(self_, **kwargs):
        """
        A single query contributing to a unit cost numerator or denominator. The accepted fields
        depend on the data source the query targets, for example ``cloud_cost`` , ``metrics`` , ``dora`` ,
        or ``ci_pipelines`` , and are passed through to the query engine unchanged.
        """
        super().__init__(kwargs)
