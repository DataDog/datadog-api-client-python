# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.detailed_finding_attributes import DetailedFindingAttributes
    from datadog_api_client.v2.model.detailed_finding_type import DetailedFindingType


class DetailedFinding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.detailed_finding_attributes import DetailedFindingAttributes
        from datadog_api_client.v2.model.detailed_finding_type import DetailedFindingType

        return {
            "attributes": (DetailedFindingAttributes,),
            "id": (str,),
            "type": (DetailedFindingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[DetailedFindingAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[DetailedFindingType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single finding with with message and resource configuration.

        :param attributes: The JSON:API attributes of the detailed finding.
        :type attributes: DetailedFindingAttributes, optional

        :param id: The unique ID for this finding.
        :type id: str, optional

        :param type: The JSON:API type for findings that have the message and resource configuration.
        :type type: DetailedFindingType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
