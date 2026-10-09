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
    from datadog_api_client.v2.model.severity_override_request_data_attributes import (
        SeverityOverrideRequestDataAttributes,
    )
    from datadog_api_client.v2.model.severity_override_request_data_relationships import (
        SeverityOverrideRequestDataRelationships,
    )
    from datadog_api_client.v2.model.severity_override_data_type import SeverityOverrideDataType


class SeverityOverrideRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_override_request_data_attributes import (
            SeverityOverrideRequestDataAttributes,
        )
        from datadog_api_client.v2.model.severity_override_request_data_relationships import (
            SeverityOverrideRequestDataRelationships,
        )
        from datadog_api_client.v2.model.severity_override_data_type import SeverityOverrideDataType

        return {
            "attributes": (SeverityOverrideRequestDataAttributes,),
            "id": (str,),
            "relationships": (SeverityOverrideRequestDataRelationships,),
            "type": (SeverityOverrideDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SeverityOverrideRequestDataAttributes,
        relationships: SeverityOverrideRequestDataRelationships,
        type: SeverityOverrideDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data of the severity override request.

        :param attributes: Attributes of the severity override request.
        :type attributes: SeverityOverrideRequestDataAttributes

        :param id: Unique identifier of the severity override request. If not provided, an identifier is generated.
        :type id: str, optional

        :param relationships: Relationships of the severity override request.
        :type relationships: SeverityOverrideRequestDataRelationships

        :param type: Severity override resource type.
        :type type: SeverityOverrideDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
