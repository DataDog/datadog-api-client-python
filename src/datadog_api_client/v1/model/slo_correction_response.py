# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.slo_correction import SLOCorrection
    from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
    from datadog_api_client.v1.model.creator import Creator
    from datadog_api_client.v1.model.slo_correction_response_attributes_modifier import (
        SLOCorrectionResponseAttributesModifier,
    )


@dataclass
class SLOCorrectionResponseJSON:
    id: str
    category: Union[SLOCorrectionCategory, UnsetType] = unset
    created_at: Union[int, none_type, UnsetType] = unset
    creator: Union[Creator, UnsetType] = unset
    description: Union[str, UnsetType] = unset
    duration: Union[int, none_type, UnsetType] = unset
    end: Union[int, none_type, UnsetType] = unset
    modified_at: Union[int, none_type, UnsetType] = unset
    modifier: Union[SLOCorrectionResponseAttributesModifier, none_type, UnsetType] = unset
    rrule: Union[str, none_type, UnsetType] = unset
    slo_id: Union[str, UnsetType] = unset
    start: Union[int, UnsetType] = unset
    timezone: Union[str, UnsetType] = unset


class SLOCorrectionResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_correction import SLOCorrection

        return {
            "data": (SLOCorrection,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = SLOCorrectionResponseJSON

    def __init__(self_, data: Union[SLOCorrection, UnsetType] = unset, **kwargs):
        """
        The response object of an SLO correction.

        :param data: The response object of a list of SLO corrections.
        :type data: SLOCorrection, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
