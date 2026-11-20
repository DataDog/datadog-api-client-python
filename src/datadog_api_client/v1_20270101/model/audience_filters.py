# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.audience_filters_accounts_items import AudienceFiltersAccountsItems
    from datadog_api_client.v1_20270101.model.audience_filters_segments_items import AudienceFiltersSegmentsItems
    from datadog_api_client.v1_20270101.model.audience_filters_users_items import AudienceFiltersUsersItems


class AudienceFilters(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.audience_filters_accounts_items import AudienceFiltersAccountsItems
        from datadog_api_client.v1_20270101.model.audience_filters_segments_items import AudienceFiltersSegmentsItems
        from datadog_api_client.v1_20270101.model.audience_filters_users_items import AudienceFiltersUsersItems

        return {
            "accounts": ([AudienceFiltersAccountsItems],),
            "segments": ([AudienceFiltersSegmentsItems],),
            "users": ([AudienceFiltersUsersItems],),
        }

    attribute_map = {
        "accounts": "accounts",
        "segments": "segments",
        "users": "users",
    }

    def __init__(
        self_,
        accounts: Union[List[AudienceFiltersAccountsItems], UnsetType] = unset,
        segments: Union[List[AudienceFiltersSegmentsItems], UnsetType] = unset,
        users: Union[List[AudienceFiltersUsersItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param accounts: Test-only generated schema for the dashboard versioning proof of concept.
        :type accounts: [AudienceFiltersAccountsItems], optional

        :param segments: Test-only generated schema for the dashboard versioning proof of concept.
        :type segments: [AudienceFiltersSegmentsItems], optional

        :param users: Test-only generated schema for the dashboard versioning proof of concept.
        :type users: [AudienceFiltersUsersItems], optional
        """
        if accounts is not unset:
            kwargs["accounts"] = accounts
        if segments is not unset:
            kwargs["segments"] = segments
        if users is not unset:
            kwargs["users"] = users
        super().__init__(kwargs)
