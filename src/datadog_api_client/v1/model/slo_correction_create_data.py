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
from datadog_api_client.v1.model.slo_correction_create_request_attributes import SLOCorrectionCreateRequestAttributes
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory

if TYPE_CHECKING:
    from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType


@dataclass
class SLOCorrectionCreateDataJSON:
    category: Union[SLOCorrectionCategory, UnsetType] = unset
    description: Union[str, UnsetType] = unset
    duration: Union[int, UnsetType] = unset
    end: Union[int, UnsetType] = unset
    rrule: Union[str, UnsetType] = unset
    slo_id: Union[str, UnsetType] = unset
    start: Union[int, UnsetType] = unset
    timezone: Union[str, UnsetType] = unset


class SLOCorrectionCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType

        return {
            "attributes": (SLOCorrectionCreateRequestAttributes,),
            "type": (SLOCorrectionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = SLOCorrectionCreateDataJSON

    def __init__(
        self_,
        type: SLOCorrectionType,
        attributes: Union[SLOCorrectionCreateRequestAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object associated with the SLO correction to be created.

        :param attributes: The attribute object associated with the SLO correction to be created.
        :type attributes: SLOCorrectionCreateRequestAttributes, optional

        :param type: SLO correction resource type.
        :type type: SLOCorrectionType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
