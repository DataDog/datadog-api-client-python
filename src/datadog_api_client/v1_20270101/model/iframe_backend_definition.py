# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.iframe_backend_definition_type import IframeBackendDefinitionType


class IframeBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.iframe_backend_definition_type import IframeBackendDefinitionType

        return {
            "type": (IframeBackendDefinitionType,),
            "url": (str,),
        }

    attribute_map = {
        "type": "type",
        "url": "url",
    }

    def __init__(self_, type: IframeBackendDefinitionType, url: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: IframeBackendDefinitionType

        :param url: Test-only generated schema for the dashboard versioning proof of concept.
        :type url: str
        """
        super().__init__(kwargs)

        self_.type = type
        self_.url = url
