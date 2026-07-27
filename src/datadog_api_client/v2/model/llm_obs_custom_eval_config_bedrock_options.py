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


class LLMObsCustomEvalConfigBedrockOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "inference_profile": (str,),
            "region": (str,),
        }

    attribute_map = {
        "inference_profile": "inference_profile",
        "region": "region",
    }

    def __init__(
        self_, inference_profile: Union[str, UnsetType] = unset, region: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        AWS Bedrock-specific options for LLM provider configuration.

        :param inference_profile: Bedrock inference profile identifier, such as an application inference profile ARN.
        :type inference_profile: str, optional

        :param region: AWS region for Bedrock.
        :type region: str, optional
        """
        if inference_profile is not unset:
            kwargs["inference_profile"] = inference_profile
        if region is not unset:
            kwargs["region"] = region
        super().__init__(kwargs)
