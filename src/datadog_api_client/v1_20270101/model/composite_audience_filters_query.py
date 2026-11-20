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
    from datadog_api_client.v1_20270101.model.composite_audience_filters_query_accounts_items import (
        CompositeAudienceFiltersQueryAccountsItems,
    )
    from datadog_api_client.v1_20270101.model.composite_audience_filters_query_data_source import (
        CompositeAudienceFiltersQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.composite_audience_filters_query_segments_items import (
        CompositeAudienceFiltersQuerySegmentsItems,
    )
    from datadog_api_client.v1_20270101.model.composite_audience_filters_query_users_items import (
        CompositeAudienceFiltersQueryUsersItems,
    )


class CompositeAudienceFiltersQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.composite_audience_filters_query_accounts_items import (
            CompositeAudienceFiltersQueryAccountsItems,
        )
        from datadog_api_client.v1_20270101.model.composite_audience_filters_query_data_source import (
            CompositeAudienceFiltersQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.composite_audience_filters_query_segments_items import (
            CompositeAudienceFiltersQuerySegmentsItems,
        )
        from datadog_api_client.v1_20270101.model.composite_audience_filters_query_users_items import (
            CompositeAudienceFiltersQueryUsersItems,
        )

        return {
            "accounts": ([CompositeAudienceFiltersQueryAccountsItems],),
            "data_source": (CompositeAudienceFiltersQueryDataSource,),
            "name": (str,),
            "segments": ([CompositeAudienceFiltersQuerySegmentsItems],),
            "users": ([CompositeAudienceFiltersQueryUsersItems],),
        }

    attribute_map = {
        "accounts": "accounts",
        "data_source": "data_source",
        "name": "name",
        "segments": "segments",
        "users": "users",
    }

    def __init__(
        self_,
        data_source: CompositeAudienceFiltersQueryDataSource,
        name: str,
        accounts: Union[List[CompositeAudienceFiltersQueryAccountsItems], UnsetType] = unset,
        segments: Union[List[CompositeAudienceFiltersQuerySegmentsItems], UnsetType] = unset,
        users: Union[List[CompositeAudienceFiltersQueryUsersItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param accounts: Test-only generated schema for the dashboard versioning proof of concept.
        :type accounts: [CompositeAudienceFiltersQueryAccountsItems], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: CompositeAudienceFiltersQueryDataSource

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param segments: Test-only generated schema for the dashboard versioning proof of concept.
        :type segments: [CompositeAudienceFiltersQuerySegmentsItems], optional

        :param users: Test-only generated schema for the dashboard versioning proof of concept.
        :type users: [CompositeAudienceFiltersQueryUsersItems], optional
        """
        if accounts is not unset:
            kwargs["accounts"] = accounts
        if segments is not unset:
            kwargs["segments"] = segments
        if users is not unset:
            kwargs["users"] = users
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
