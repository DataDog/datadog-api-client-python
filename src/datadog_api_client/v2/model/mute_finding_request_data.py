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
    from datadog_api_client.v2.model.mute_finding_request_attributes import MuteFindingRequestAttributes
    from datadog_api_client.v2.model.finding_type import FindingType


class MuteFindingRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_finding_request_attributes import MuteFindingRequestAttributes
        from datadog_api_client.v2.model.finding_type import FindingType

        return {
            "attributes": (MuteFindingRequestAttributes,),
            "id": (str,),
            "type": (FindingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: MuteFindingRequestAttributes, id: str, type: FindingType, **kwargs):
        """
        Data object containing the new mute properties of the finding.

        :param attributes: The mute properties to be updated.
        :type attributes: MuteFindingRequestAttributes

        :param id: The unique ID for this finding.
        :type id: str

        :param type: The JSON:API type for findings.
        :type type: FindingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
