# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricSearchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.metric_search_response_results import MetricSearchResponseResults

        return {
            "results": (MetricSearchResponseResults,),
        }

    attribute_map = {
        "results": "results",
    }

    def __init__(self_, *args, **kwargs):
        """
        Object containing the list of metrics matching the search query.

        :param results: Search result.
        :type results: MetricSearchResponseResults, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
