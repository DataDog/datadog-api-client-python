# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AccountFiltersType(ModelSimple):
    """
    Type of account filters.

    :param value: If omitted defaults to "account_filters". Must be one of ["account_filters"].
    :type value: str
    """

    allowed_values = {
        "account_filters",
    }
    ACCOUNT_FILTERS: ClassVar["AccountFiltersType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AccountFiltersType.ACCOUNT_FILTERS = AccountFiltersType("account_filters")
