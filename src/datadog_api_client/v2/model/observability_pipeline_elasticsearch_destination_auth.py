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
    from datadog_api_client.v2.model.observability_pipeline_amazon_open_search_destination_auth_strategy import (
        ObservabilityPipelineAmazonOpenSearchDestinationAuthStrategy,
    )


class ObservabilityPipelineElasticsearchDestinationAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_amazon_open_search_destination_auth_strategy import (
            ObservabilityPipelineAmazonOpenSearchDestinationAuthStrategy,
        )

        return {
            "password_key": (str,),
            "strategy": (ObservabilityPipelineAmazonOpenSearchDestinationAuthStrategy,),
            "username_key": (str,),
        }

    attribute_map = {
        "password_key": "password_key",
        "strategy": "strategy",
        "username_key": "username_key",
    }

    def __init__(
        self_,
        strategy: ObservabilityPipelineAmazonOpenSearchDestinationAuthStrategy,
        password_key: Union[str, UnsetType] = unset,
        username_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Authentication settings for the Elasticsearch destination.
        When ``strategy`` is ``basic`` , use ``username_key`` and ``password_key`` to reference credentials stored in environment variables or secrets.

        :param password_key: Name of the environment variable or secret that holds the Elasticsearch password (used when ``strategy`` is ``basic`` ).
        :type password_key: str, optional

        :param strategy: The authentication strategy to use.
        :type strategy: ObservabilityPipelineAmazonOpenSearchDestinationAuthStrategy

        :param username_key: Name of the environment variable or secret that holds the Elasticsearch username (used when ``strategy`` is ``basic`` ).
        :type username_key: str, optional
        """
        if password_key is not unset:
            kwargs["password_key"] = password_key
        if username_key is not unset:
            kwargs["username_key"] = username_key
        super().__init__(kwargs)

        self_.strategy = strategy
