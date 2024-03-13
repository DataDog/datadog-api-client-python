# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_destination_response_elasticsearch_destination_auth import (
        CustomDestinationResponseElasticsearchDestinationAuth,
    )
    from datadog_api_client.v2.model.custom_destination_response_forward_destination_elasticsearch_type import (
        CustomDestinationResponseForwardDestinationElasticsearchType,
    )


class CustomDestinationResponseForwardDestinationElasticsearch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_response_elasticsearch_destination_auth import (
            CustomDestinationResponseElasticsearchDestinationAuth,
        )
        from datadog_api_client.v2.model.custom_destination_response_forward_destination_elasticsearch_type import (
            CustomDestinationResponseForwardDestinationElasticsearchType,
        )

        return {
            "auth": (CustomDestinationResponseElasticsearchDestinationAuth,),
            "endpoint": (str,),
            "index_name": (str,),
            "index_rotation": (str,),
            "type": (CustomDestinationResponseForwardDestinationElasticsearchType,),
        }

    attribute_map = {
        "auth": "auth",
        "endpoint": "endpoint",
        "index_name": "index_name",
        "index_rotation": "index_rotation",
        "type": "type",
    }

    def __init__(
        self_,
        auth: CustomDestinationResponseElasticsearchDestinationAuth,
        endpoint: str,
        index_name: str,
        type: CustomDestinationResponseForwardDestinationElasticsearchType,
        index_rotation: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The Elasticsearch destination.

        :param auth: Basic access authentication.
        :type auth: CustomDestinationResponseElasticsearchDestinationAuth

        :param endpoint: The destination for which logs will be forwarded to.
            Must have HTTPS scheme and forwarding back to Datadog is not allowed.
        :type endpoint: str

        :param index_name: Name of the Elasticsearch index (must follow `Elasticsearch's criteria <https://www.elastic.co/guide/en/elasticsearch/reference/8.11/indices-create-index.html#indices-create-api-path-params>`_ ).
        :type index_name: str

        :param index_rotation: Date pattern with US locale and UTC timezone to be appended to the index name after adding ``-``
            (that is, ``${index_name}-${indexPattern}`` ).
            You can customize the index rotation naming pattern by choosing one of these options:

            * Hourly: ``yyyy-MM-dd-HH`` (as an example, it would render: ``2022-10-19-09`` )
            * Daily: ``yyyy-MM-dd`` (as an example, it would render: ``2022-10-19`` )
            * Weekly: ``yyyy-'W'ww`` (as an example, it would render: ``2022-W42`` )
            * Monthly: ``yyyy-MM`` (as an example, it would render: ``2022-10`` )

            If this field is missing or is blank, it means that the index name will always be the same
            (that is, no rotation).
        :type index_rotation: str, optional

        :param type: Type of the Elasticsearch destination.
        :type type: CustomDestinationResponseForwardDestinationElasticsearchType
        """
        if index_rotation is not unset:
            kwargs["index_rotation"] = index_rotation
        super().__init__(kwargs)

        self_.auth = auth
        self_.endpoint = endpoint
        self_.index_name = index_name
        self_.type = type
