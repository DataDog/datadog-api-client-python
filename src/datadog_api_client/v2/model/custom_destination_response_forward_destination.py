# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class CustomDestinationResponseForwardDestination(ModelComposed):
    def __init__(self, **kwargs):
        """
        A custom destination's location to forward logs.

        :param auth: Authentication method of the HTTP requests.
        :type auth: CustomDestinationResponseHttpDestinationAuth

        :param endpoint: The destination for which logs will be forwarded to.
            Must have HTTPS scheme and forwarding back to Datadog is not allowed.
        :type endpoint: str

        :param type: Type of the HTTP destination.
        :type type: CustomDestinationResponseForwardDestinationHttpType

        :param index_name: Name of the Elasticsearch index (must follow [Elasticsearch's criteria](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params)).
        :type index_name: str

        :param index_rotation: Date pattern with US locale and UTC timezone to be appended to the index name after adding `-`
            (that is, `${index_name}-${indexPattern}`).
            You can customize the index rotation naming pattern by choosing one of these options:
            - Hourly: `yyyy-MM-dd-HH` (as an example, it would render: `2022-10-19-09`)
            - Daily: `yyyy-MM-dd` (as an example, it would render: `2022-10-19`)
            - Weekly: `yyyy-'W'ww` (as an example, it would render: `2022-W42`)
            - Monthly: `yyyy-MM` (as an example, it would render: `2022-10`)

            If this field is missing or is blank, it means that the index name will always be the same
            (that is, no rotation).
        :type index_rotation: str, optional
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
        from datadog_api_client.v2.model.custom_destination_response_forward_destination_http import (
            CustomDestinationResponseForwardDestinationHttp,
        )
        from datadog_api_client.v2.model.custom_destination_response_forward_destination_splunk import (
            CustomDestinationResponseForwardDestinationSplunk,
        )
        from datadog_api_client.v2.model.custom_destination_response_forward_destination_elasticsearch import (
            CustomDestinationResponseForwardDestinationElasticsearch,
        )

        return {
            "oneOf": [
                CustomDestinationResponseForwardDestinationHttp,
                CustomDestinationResponseForwardDestinationSplunk,
                CustomDestinationResponseForwardDestinationElasticsearch,
            ],
        }
