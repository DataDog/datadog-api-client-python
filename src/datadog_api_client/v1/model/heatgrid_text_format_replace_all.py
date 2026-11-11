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
    from datadog_api_client.v1.model.heatgrid_text_format_replace_all_type import HeatgridTextFormatReplaceAllType


class HeatgridTextFormatReplaceAll(ModelNormal):
    validations = {
        "_with": {
            "max_length": 255,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_text_format_replace_all_type import HeatgridTextFormatReplaceAllType

        return {
            "type": (HeatgridTextFormatReplaceAllType,),
            "_with": (str,),
        }

    attribute_map = {
        "type": "type",
        "_with": "with",
    }

    def __init__(self_, type: HeatgridTextFormatReplaceAllType, _with: str, **kwargs):
        """
        Replace the entire matching group label.

        :param type: Replace the entire matching group label.
        :type type: HeatgridTextFormatReplaceAllType

        :param _with: Replacement string.
        :type _with: str
        """
        super().__init__(kwargs)

        self_.type = type
        self_._with = _with
