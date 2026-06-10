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
    from datadog_api_client.v2.model.ownership_evidence_attributes import OwnershipEvidenceAttributes
    from datadog_api_client.v2.model.ownership_evidence_type import OwnershipEvidenceType


class OwnershipEvidenceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_evidence_attributes import OwnershipEvidenceAttributes
        from datadog_api_client.v2.model.ownership_evidence_type import OwnershipEvidenceType

        return {
            "attributes": (OwnershipEvidenceAttributes,),
            "id": (str,),
            "type": (OwnershipEvidenceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OwnershipEvidenceAttributes, id: str, type: OwnershipEvidenceType, **kwargs):
        """
        The data wrapper for an ownership evidence response.

        :param attributes: The attributes of an ownership evidence response.
        :type attributes: OwnershipEvidenceAttributes

        :param id: The identifier of the resource the evidence applies to.
        :type id: str

        :param type: The type of the ownership evidence resource. The value should always be ``ownership_evidence``.
        :type type: OwnershipEvidenceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
