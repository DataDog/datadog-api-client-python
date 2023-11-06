# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class CostByOrgType(StringEnum):
    """
    Type of cost data.

    :param value: If omitted defaults to "cost_by_org". Must be one of ["cost_by_org"].
    :type value: str
    """

    allowed_values = {
        "cost_by_org",
    }
    COST_BY_ORG: ClassVar["CostByOrgType"]


CostByOrgType.COST_BY_ORG = CostByOrgType("cost_by_org")
