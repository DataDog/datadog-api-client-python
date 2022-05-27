# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMAnalyticsAggregateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_aggregation_buckets_response import RUMAggregationBucketsResponse
        from datadog_api_client.v2.model.rum_response_links import RUMResponseLinks
        from datadog_api_client.v2.model.rum_response_metadata import RUMResponseMetadata

        return {
            "data": (RUMAggregationBucketsResponse,),
            "links": (RUMResponseLinks,),
            "meta": (RUMResponseMetadata,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(self, *args, **kwargs):
        """
        The response object for the RUM events aggregate API endpoint.

        :param data: The query results.
        :type data: RUMAggregationBucketsResponse, optional

        :param links: Links attributes.
        :type links: RUMResponseLinks, optional

        :param meta: The metadata associated with a request.
        :type meta: RUMResponseMetadata, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RUMAnalyticsAggregateResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
