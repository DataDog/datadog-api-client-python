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


class LLMObsAzureOpenAIMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "deployment_id": (str,),
            "model_version": (str,),
            "resource_name": (str,),
        }

    attribute_map = {
        "deployment_id": "deployment_id",
        "model_version": "model_version",
        "resource_name": "resource_name",
    }

    def __init__(
        self_,
        deployment_id: Union[str, UnsetType] = unset,
        model_version: Union[str, UnsetType] = unset,
        resource_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Azure OpenAI-specific metadata for an integration account or inference request.

        :param deployment_id: The Azure OpenAI deployment ID.
        :type deployment_id: str, optional

        :param model_version: The model version deployed in Azure.
        :type model_version: str, optional

        :param resource_name: The Azure OpenAI resource name.
        :type resource_name: str, optional
        """
        if deployment_id is not unset:
            kwargs["deployment_id"] = deployment_id
        if model_version is not unset:
            kwargs["model_version"] = model_version
        if resource_name is not unset:
            kwargs["resource_name"] = resource_name
        super().__init__(kwargs)
