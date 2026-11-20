# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class GeomapBackendRegionsRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: GeomapBackendRegionsRequestAnyOfAnyOfItemResponseFormat

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: GeomapRequestStyle, optional

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: GeomapBackendRegionsRequestAnyOfAnyOfItemRequestType

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema6, none_type,)}, optional

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str

        :param log_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type log_query: LogQueryDefinition

        :param apm_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type apm_query: LogQueryDefinition

        :param network_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type network_query: LogQueryDefinition

        :param rum_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type rum_query: LogQueryDefinition

        :param security_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type security_query: LogQueryDefinition

        :param compliance_findings_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type compliance_findings_query: LogQueryDefinition

        :param event_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type event_query: LogQueryDefinition

        :param profile_metrics_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type profile_metrics_query: LogQueryDefinition

        :param ci_pipeline_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ci_pipeline_query: LogQueryDefinition

        :param ci_test_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ci_test_query: LogQueryDefinition

        :param audit_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type audit_query: LogQueryDefinition

        :param appsecspan_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type appsecspan_query: LogQueryDefinition

        :param synthetics_batches: Test-only generated schema for the dashboard versioning proof of concept.
        :type synthetics_batches: LogQueryDefinition

        :param synthetics_test_runs: Test-only generated schema for the dashboard versioning proof of concept.
        :type synthetics_test_runs: LogQueryDefinition

        :param profilemetrics_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type profilemetrics_query: LogQueryDefinition
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
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of import (
            GeomapBackendRegionsRequest20270101OneOf,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457233792 import (
            GeomapBackendRegionsRequest20270101OneOf4457233792,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457448128 import (
            GeomapBackendRegionsRequest20270101OneOf4457448128,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457449888 import (
            GeomapBackendRegionsRequest20270101OneOf4457449888,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457450848 import (
            GeomapBackendRegionsRequest20270101OneOf4457450848,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457451808 import (
            GeomapBackendRegionsRequest20270101OneOf4457451808,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457452768 import (
            GeomapBackendRegionsRequest20270101OneOf4457452768,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457453728 import (
            GeomapBackendRegionsRequest20270101OneOf4457453728,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457454688 import (
            GeomapBackendRegionsRequest20270101OneOf4457454688,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457455648 import (
            GeomapBackendRegionsRequest20270101OneOf4457455648,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457456608 import (
            GeomapBackendRegionsRequest20270101OneOf4457456608,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457457568 import (
            GeomapBackendRegionsRequest20270101OneOf4457457568,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457458528 import (
            GeomapBackendRegionsRequest20270101OneOf4457458528,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457459488 import (
            GeomapBackendRegionsRequest20270101OneOf4457459488,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457460448 import (
            GeomapBackendRegionsRequest20270101OneOf4457460448,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457461408 import (
            GeomapBackendRegionsRequest20270101OneOf4457461408,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457462368 import (
            GeomapBackendRegionsRequest20270101OneOf4457462368,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457463328 import (
            GeomapBackendRegionsRequest20270101OneOf4457463328,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_regions_request20270101_one_of4457645216 import (
            GeomapBackendRegionsRequest20270101OneOf4457645216,
        )

        return {
            "oneOf": [
                GeomapBackendRegionsRequest20270101OneOf,
                GeomapBackendRegionsRequest20270101OneOf4457233792,
                GeomapBackendRegionsRequest20270101OneOf4457448128,
                GeomapBackendRegionsRequest20270101OneOf4457449888,
                GeomapBackendRegionsRequest20270101OneOf4457450848,
                GeomapBackendRegionsRequest20270101OneOf4457451808,
                GeomapBackendRegionsRequest20270101OneOf4457452768,
                GeomapBackendRegionsRequest20270101OneOf4457453728,
                GeomapBackendRegionsRequest20270101OneOf4457454688,
                GeomapBackendRegionsRequest20270101OneOf4457455648,
                GeomapBackendRegionsRequest20270101OneOf4457456608,
                GeomapBackendRegionsRequest20270101OneOf4457457568,
                GeomapBackendRegionsRequest20270101OneOf4457458528,
                GeomapBackendRegionsRequest20270101OneOf4457459488,
                GeomapBackendRegionsRequest20270101OneOf4457460448,
                GeomapBackendRegionsRequest20270101OneOf4457461408,
                GeomapBackendRegionsRequest20270101OneOf4457462368,
                GeomapBackendRegionsRequest20270101OneOf4457463328,
                GeomapBackendRegionsRequest20270101OneOf4457645216,
            ],
        }
