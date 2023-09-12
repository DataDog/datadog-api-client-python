# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class CustomDestinationForwarderDestination(ModelComposed):
    def __init__(self, **kwargs):
        """
        The destination to forward events to.

        :param auth: The authentication method used for HTTP destinations.
        :type auth: HttpDestinationAuth

        :param endpoint: The intake URL to forward events to.
        :type endpoint: str

        :param type: The HTTP destination type.
        :type type: HttpDestinationType

        :param index_name: The Elasticsearch index name.
        :type index_name: str

        :param index_rotation: The pattern to append to the index name for rotation in Elasticsearch.
        :type index_rotation: str

        :param access_token: The access token of the Splunk destination.
        :type access_token: str
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
        from datadog_api_client.v2.model.http_destination import HttpDestination
        from datadog_api_client.v2.model.elasticsearch_destination import ElasticsearchDestination
        from datadog_api_client.v2.model.splunk_hec_destination import SplunkHecDestination

        return {
            "oneOf": [
                HttpDestination,
                ElasticsearchDestination,
                SplunkHecDestination,
            ],
        }
