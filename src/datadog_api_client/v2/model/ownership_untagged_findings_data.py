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
    from datadog_api_client.v2.model.ownership_untagged_findings_attributes import OwnershipUntaggedFindingsAttributes
    from datadog_api_client.v2.model.ownership_untagged_findings_type import OwnershipUntaggedFindingsType


class OwnershipUntaggedFindingsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_untagged_findings_attributes import (
            OwnershipUntaggedFindingsAttributes,
        )
        from datadog_api_client.v2.model.ownership_untagged_findings_type import OwnershipUntaggedFindingsType

        return {
            "attributes": (OwnershipUntaggedFindingsAttributes,),
            "id": (str,),
            "type": (OwnershipUntaggedFindingsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: OwnershipUntaggedFindingsAttributes, id: str, type: OwnershipUntaggedFindingsType, **kwargs
    ):
        """
        The data wrapper for an ownership untagged findings response.

        :param attributes: The counts of findings without a team tag by ownership confidence.
        :type attributes: OwnershipUntaggedFindingsAttributes

        :param id: The identifier of the ownership untagged findings resource.
        :type id: str

        :param type: The type of the ownership untagged findings resource. The value should always be ``ownership_untagged_findings``.
        :type type: OwnershipUntaggedFindingsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
