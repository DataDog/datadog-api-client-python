# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class LLMObsBedrockMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "region": (str,),
        }

    attribute_map = {
        "region": "region",
    }

    def __init__(self_, region: Union[str, UnsetType] = unset, **kwargs):
        """
        Amazon Bedrock-specific metadata for an inference request.

        :param region: The AWS region for the Bedrock request.
        :type region: str, optional
        """
        if region is not unset:
            kwargs["region"] = region
        super().__init__(kwargs)
