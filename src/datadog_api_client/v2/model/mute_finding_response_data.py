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
    from datadog_api_client.v2.model.mute_finding_response_attributes import MuteFindingResponseAttributes
    from datadog_api_client.v2.model.finding_type import FindingType


class MuteFindingResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_finding_response_attributes import MuteFindingResponseAttributes
        from datadog_api_client.v2.model.finding_type import FindingType

        return {
            "attributes": (MuteFindingResponseAttributes,),
            "id": (str,),
            "type": (FindingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[MuteFindingResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[FindingType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object containing the updated finding.

        :param attributes: The JSON:API attributes of the finding.
        :type attributes: MuteFindingResponseAttributes, optional

        :param id: The unique ID for this finding.
        :type id: str, optional

        :param type: The JSON:API type for findings.
        :type type: FindingType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
