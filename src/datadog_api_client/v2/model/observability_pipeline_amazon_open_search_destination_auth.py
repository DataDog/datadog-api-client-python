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


class ObservabilityPipelineAmazonOpenSearchDestinationAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_amazon_open_search_destination_auth_strategy import (
            ObservabilityPipelineAmazonOpenSearchDestinationAuthStrategy,
        )

        return {
            "assume_role": (str,),
            "aws_region": (str,),
            "external_id": (str,),
            "session_name": (str,),
            "strategy": (ObservabilityPipelineAmazonOpenSearchDestinationAuthStrategy,),
        }

    attribute_map = {
        "assume_role": "assume_role",
        "aws_region": "aws_region",
        "external_id": "external_id",
        "session_name": "session_name",
        "strategy": "strategy",
    }

    def __init__(
        self_,
        strategy: ObservabilityPipelineAmazonOpenSearchDestinationAuthStrategy,
        assume_role: Union[str, UnsetType] = unset,
        aws_region: Union[str, UnsetType] = unset,
        external_id: Union[str, UnsetType] = unset,
        session_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Authentication settings for the Amazon OpenSearch destination.
        The ``strategy`` field determines whether basic or AWS-based authentication is used.

        :param assume_role: The ARN of the role to assume (used with ``aws`` strategy).
        :type assume_role: str, optional

        :param aws_region: AWS region
        :type aws_region: str, optional

        :param external_id: External ID for the assumed role (used with ``aws`` strategy).
        :type external_id: str, optional

        :param session_name: Session name for the assumed role (used with ``aws`` strategy).
        :type session_name: str, optional

        :param strategy: The authentication strategy to use.
        :type strategy: ObservabilityPipelineAmazonOpenSearchDestinationAuthStrategy
        """
        if assume_role is not unset:
            kwargs["assume_role"] = assume_role
        if aws_region is not unset:
            kwargs["aws_region"] = aws_region
        if external_id is not unset:
            kwargs["external_id"] = external_id
        if session_name is not unset:
            kwargs["session_name"] = session_name
        super().__init__(kwargs)

        self_.strategy = strategy
