# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.zoom_configuration_reference_data import ZoomConfigurationReferenceData


class ZoomConfigurationReference(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.zoom_configuration_reference_data import ZoomConfigurationReferenceData

        return {
            "data": (ZoomConfigurationReferenceData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[ZoomConfigurationReferenceData, none_type], **kwargs):
        """
        A reference to a Zoom configuration resource.

        :param data: The Zoom configuration relationship data object.
        :type data: ZoomConfigurationReferenceData, none_type
        """
        super().__init__(kwargs)

        self_.data = data
