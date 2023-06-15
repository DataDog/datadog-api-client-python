# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory

if TYPE_CHECKING:
    from datadog_api_client.v1.model.slo_correction_create_data import SLOCorrectionCreateData


@dataclass
class SLOCorrectionCreateRequestJSON:
    category: Union[SLOCorrectionCategory, UnsetType] = unset
    description: Union[str, UnsetType] = unset
    duration: Union[int, UnsetType] = unset
    end: Union[int, UnsetType] = unset
    rrule: Union[str, UnsetType] = unset
    slo_id: Union[str, UnsetType] = unset
    start: Union[int, UnsetType] = unset
    timezone: Union[str, UnsetType] = unset


class SLOCorrectionCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_correction_create_data import SLOCorrectionCreateData

        return {
            "data": (SLOCorrectionCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = SLOCorrectionCreateRequestJSON

    def __init__(self_, data: Union[SLOCorrectionCreateData, UnsetType] = unset, **kwargs):
        """
        An object that defines a correction to be applied to an SLO.

        :param data: The data object associated with the SLO correction to be created.
        :type data: SLOCorrectionCreateData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
