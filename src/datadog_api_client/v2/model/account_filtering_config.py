# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AccountFilteringConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "excluded_accounts": ([str],),
            "include_new_accounts": (bool,),
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
        include_new_accounts: Union[bool, UnsetType] = unset,
        included_accounts: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The account filtering configuration.

        :param excluded_accounts: The AWS account IDs to be excluded from your billing dataset. This field is used when ``include_new_accounts`` is ``true``.
        :type excluded_accounts: [str], optional

        :param include_new_accounts: Whether or not to automatically include new member accounts by default in your billing dataset.
        :type include_new_accounts: bool, optional

        :param included_accounts: The AWS account IDs to be included in your billing dataset. This field is used when ``include_new_accounts`` is ``false``.
        :type included_accounts: [str], optional
        """
        if excluded_accounts is not unset:
            kwargs["excluded_accounts"] = excluded_accounts
        if include_new_accounts is not unset:
            kwargs["include_new_accounts"] = include_new_accounts
        if included_accounts is not unset:
            kwargs["included_accounts"] = included_accounts
        super().__init__(kwargs)
