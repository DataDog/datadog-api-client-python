# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class AwsCurConfigResponseDataAttributesAccountFilters(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "excluded_accounts": ([str],),
            "include_new_accounts": (bool, none_type),
            "included_accounts": ([str],),
        }

    attribute_map = {
        "excluded_accounts": "excluded_accounts",
        "include_new_accounts": "include_new_accounts",
        "included_accounts": "included_accounts",
    }

    def __init__(
        self_,
        excluded_accounts: Union[List[str], UnsetType] = unset,
        include_new_accounts: Union[bool, none_type, UnsetType] = unset,
        included_accounts: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``AwsCurConfigResponseDataAttributesAccountFilters`` object.

        :param excluded_accounts: The ``account_filters`` ``excluded_accounts``.
        :type excluded_accounts: [str], optional

        :param include_new_accounts: The ``account_filters`` ``include_new_accounts``.
        :type include_new_accounts: bool, none_type, optional

        :param included_accounts: The ``account_filters`` ``included_accounts``.
        :type included_accounts: [str], optional
        """
        if excluded_accounts is not unset:
            kwargs["excluded_accounts"] = excluded_accounts
        if include_new_accounts is not unset:
            kwargs["include_new_accounts"] = include_new_accounts
        if included_accounts is not unset:
            kwargs["included_accounts"] = included_accounts
        super().__init__(kwargs)
