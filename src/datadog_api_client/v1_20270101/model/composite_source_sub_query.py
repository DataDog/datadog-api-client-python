# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class CompositeSourceSubQuery(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [ListColumn], optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [AggregateCompute]

        :param compute_count: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute_count: bool, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaAndFunctionEventsDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [FormulaAndFunctionEventQueryGroupBy]

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: CompositeEventsPlatformSubQueryDefinitionSearch, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param table_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type table_name: str

        :param accounts: Test-only generated schema for the dashboard versioning proof of concept.
        :type accounts: [CompositeAudienceFiltersQueryAccountsItems], optional

        :param segments: Test-only generated schema for the dashboard versioning proof of concept.
        :type segments: [CompositeAudienceFiltersQuerySegmentsItems], optional

        :param users: Test-only generated schema for the dashboard versioning proof of concept.
        :type users: [CompositeAudienceFiltersQueryUsersItems], optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1_20270101.model.composite_events_platform_sub_query_definition import (
            CompositeEventsPlatformSubQueryDefinition,
        )
        from datadog_api_client.v1_20270101.model.composite_referential_data_query import CompositeReferentialDataQuery
        from datadog_api_client.v1_20270101.model.composite_audience_filters_query import CompositeAudienceFiltersQuery

        return {
            "oneOf": [
                CompositeEventsPlatformSubQueryDefinition,
                CompositeReferentialDataQuery,
                CompositeAudienceFiltersQuery,
            ],
        }
