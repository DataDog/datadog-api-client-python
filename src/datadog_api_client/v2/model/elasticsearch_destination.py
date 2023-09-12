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
    from datadog_api_client.v2.model.http_destination_basic_auth import HttpDestinationBasicAuth
    from datadog_api_client.v2.model.elasticsearch_destination_type import ElasticsearchDestinationType


class ElasticsearchDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_destination_basic_auth import HttpDestinationBasicAuth
        from datadog_api_client.v2.model.elasticsearch_destination_type import ElasticsearchDestinationType

        return {
            "auth": (HttpDestinationBasicAuth,),
            "endpoint": (str,),
            "index_name": (str,),
            "index_rotation": (str,),
            "type": (ElasticsearchDestinationType,),
        }

    attribute_map = {
        "auth": "auth",
        "endpoint": "endpoint",
        "index_name": "indexName",
        "index_rotation": "indexRotation",
        "type": "type",
    }

    def __init__(
        self_,
        endpoint: str,
        index_name: str,
        index_rotation: str,
        type: ElasticsearchDestinationType,
        auth: Union[HttpDestinationBasicAuth, UnsetType] = unset,
        **kwargs,
    ):
        """
        The Elasticsearch destination.

        :param auth: The HTTP destination basic username and password auth.
        :type auth: HttpDestinationBasicAuth, optional

        :param endpoint: The intake URL to forward events to.
        :type endpoint: str

        :param index_name: The Elasticsearch index name.
        :type index_name: str

        :param index_rotation: The pattern to append to the index name for rotation in Elasticsearch.
        :type index_rotation: str

        :param type: The Elasticsearch destination type.
        :type type: ElasticsearchDestinationType
        """
        if auth is not unset:
            kwargs["auth"] = auth
        super().__init__(kwargs)

        self_.endpoint = endpoint
        self_.index_name = index_name
        self_.index_rotation = index_rotation
        self_.type = type
