# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TopologyQuery(ModelNormal):
    validations = {
        "filters": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_query_data_source import TopologyQueryDataSource

        return {
            "data_source": (TopologyQueryDataSource,),
            "filters": ([str],),
            "service": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "filters": "filters",
        "service": "service",
    }

    def __init__(self_, *args, **kwargs):
        """
        Query to service-based topology data sources like the service map or data streams.

        :param data_source: Name of the data source
        :type data_source: TopologyQueryDataSource, optional

        :param filters: Your environment and primary tag (or * if enabled for your account).
        :type filters: [str], optional

        :param service: Name of the service
        :type service: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
