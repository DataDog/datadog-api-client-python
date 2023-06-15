# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
from datadog_api_client.v1.model.creator import Creator
from datadog_api_client.v1.model.slo_correction_response_attributes_modifier import (
    SLOCorrectionResponseAttributesModifier,
)
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
from datadog_api_client.v1.model.creator import Creator
from datadog_api_client.v1.model.slo_correction_response_attributes_modifier import (
    SLOCorrectionResponseAttributesModifier,
)

if TYPE_CHECKING:
    from datadog_api_client.v1.model.slo_correction import SLOCorrection
    from datadog_api_client.v1.model.response_meta_attributes import ResponseMetaAttributes


@dataclass
class SLOCorrectionListResponseJSON:
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


class SLOCorrectionListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_correction import SLOCorrection
        from datadog_api_client.v1.model.response_meta_attributes import ResponseMetaAttributes

        return {
            "data": ([SLOCorrection],),
            "meta": (ResponseMetaAttributes,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }
    json_api_model = SLOCorrectionListResponseJSON

    def __init__(
        self_,
        data: Union[List[SLOCorrection], UnsetType] = unset,
        meta: Union[ResponseMetaAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        A list of  SLO correction objects.

        :param data: The list of of SLO corrections objects.
        :type data: [SLOCorrection], optional

        :param meta: Object describing meta attributes of response.
        :type meta: ResponseMetaAttributes, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
