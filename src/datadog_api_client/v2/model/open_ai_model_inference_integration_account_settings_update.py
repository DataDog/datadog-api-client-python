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


class OpenAIModelInferenceIntegrationAccountSettingsUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "custom_tags": (str,),
        }

    attribute_map = {
        "custom_tags": "custom_tags",
    }

    def __init__(self_, custom_tags: Union[str, UnsetType] = unset, **kwargs):
        """
        Settings for updating the OpenAI Model Inference integration account. Only the fields provided are changed.

        :param custom_tags: Comma-separated list of custom tags applied to the data collected for this account, for example ``team:ai,env:prod``.
        :type custom_tags: str, optional
        """
        if custom_tags is not unset:
            kwargs["custom_tags"] = custom_tags
        super().__init__(kwargs)
