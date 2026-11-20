# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class FormulaApmStatsQuery(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaApmDependencyStatsQueryDataSource

        :param env: Test-only generated schema for the dashboard versioning proof of concept.
        :type env: str

        :param is_upstream: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_upstream: bool, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param operation_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type operation_name: str

        :param primary_tag_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type primary_tag_name: str, optional

        :param primary_tag_value: Test-only generated schema for the dashboard versioning proof of concept.
        :type primary_tag_value: str, optional

        :param resource_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type resource_name: str

        :param service: Test-only generated schema for the dashboard versioning proof of concept.
        :type service: str

        :param stat: Test-only generated schema for the dashboard versioning proof of concept.
        :type stat: ApmDependencyStat

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [str]

        :param peer_service: Test-only generated schema for the dashboard versioning proof of concept.
        :type peer_service: str, optional

        :param version: Test-only generated schema for the dashboard versioning proof of concept.
        :type version: str, optional
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
        from datadog_api_client.v1_20270101.model.formula_apm_dependency_stats_query import (
            FormulaApmDependencyStatsQuery,
        )
        from datadog_api_client.v1_20270101.model.formula_apm_resource_stats_query import FormulaApmResourceStatsQuery

        return {
            "oneOf": [
                FormulaApmDependencyStatsQuery,
                FormulaApmResourceStatsQuery,
            ],
        }
