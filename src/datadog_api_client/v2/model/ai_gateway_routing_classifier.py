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


class AiGatewayRoutingClassifier(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "confidence_threshold": (float,),
            "context": (str,),
            "model": (str,),
            "provider": (str,),
        }

    attribute_map = {
        "confidence_threshold": "confidence_threshold",
        "context": "context",
        "model": "model",
        "provider": "provider",
    }

    def __init__(
        self_, confidence_threshold: float, model: str, provider: str, context: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Saved classified-tier settings. Provider and model are empty when the caller cannot view the provider.

        :param confidence_threshold: Minimum decision confidence.
        :type confidence_threshold: float

        :param context: Traffic context for the classifier.
        :type context: str, optional

        :param model: Viewable decision model, or an empty string.
        :type model: str

        :param provider: Viewable decision-model provider slug, or an empty string.
        :type provider: str
        """
        if context is not unset:
            kwargs["context"] = context
        super().__init__(kwargs)

        self_.confidence_threshold = confidence_threshold
        self_.model = model
        self_.provider = provider
