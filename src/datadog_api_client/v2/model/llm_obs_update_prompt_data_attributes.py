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


class LLMObsUpdatePromptDataAttributes(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "title": (str,),
        }

    attribute_map = {
        "description": "description",
        "title": "title",
    }

    def __init__(self_, description: Union[str, UnsetType] = unset, title: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes for updating an LLM Observability prompt. At least one of ``title`` or ``description`` must be provided; both attributes are optional individually.

        :param description: Optional new description for the prompt.
        :type description: str, optional

        :param title: Optional new title for the prompt.
        :type title: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
