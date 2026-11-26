# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class GeomapBackendPointsRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [GeomapBackendPointsRequestAnyOfAnyOfItemColumnsItems]

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: LogsStreamQuery

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: GeomapBackendPointsRequestAnyOfAnyOfItemResponseFormat

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: GeomapRequestStyle, optional

        :param text_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_formats: [TextFormattingRule], optional

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: GeomapBackendPointsRequestAnyOfAnyOfItemRequestType

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: GeomapPointsProjection
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
        from datadog_api_client.v1_20270101.model.geomap_backend_points_request20270101_one_of import (
            GeomapBackendPointsRequest20270101OneOf,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_points_request20270101_one_of4457225472 import (
            GeomapBackendPointsRequest20270101OneOf4457225472,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_points_request20270101_one_of4457227232 import (
            GeomapBackendPointsRequest20270101OneOf4457227232,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_points_request20270101_one_of4457228992 import (
            GeomapBackendPointsRequest20270101OneOf4457228992,
        )
        from datadog_api_client.v1_20270101.model.geomap_backend_points_request20270101_one_of4457230272 import (
            GeomapBackendPointsRequest20270101OneOf4457230272,
        )

        return {
            "oneOf": [
                GeomapBackendPointsRequest20270101OneOf,
                GeomapBackendPointsRequest20270101OneOf4457225472,
                GeomapBackendPointsRequest20270101OneOf4457227232,
                GeomapBackendPointsRequest20270101OneOf4457228992,
                GeomapBackendPointsRequest20270101OneOf4457230272,
            ],
        }
