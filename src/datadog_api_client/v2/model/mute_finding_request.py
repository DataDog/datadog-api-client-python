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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.mute_finding_request_data import MuteFindingRequestData
    from datadog_api_client.v2.model.mute_finding_request_properties import MuteFindingRequestProperties


@dataclass
class MuteFindingRequestJSON:
    id: str
    mute: Union[MuteFindingRequestProperties, UnsetType] = unset


class MuteFindingRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_finding_request_data import MuteFindingRequestData

        return {
            "data": (MuteFindingRequestData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MuteFindingRequestJSON

    def __init__(self_, data: MuteFindingRequestData, **kwargs):
        """
        The new mute finding request.

        :param data: Data object containing the new mute properties of the finding.
        :type data: MuteFindingRequestData
        """
        super().__init__(kwargs)

        self_.data = data
