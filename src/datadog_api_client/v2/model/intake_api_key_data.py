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
    from datadog_api_client.v2.model.intake_api_key_attributes import IntakeAPIKeyAttributes
    from datadog_api_client.v2.model.intake_api_key_type import IntakeAPIKeyType


class IntakeAPIKeyData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.intake_api_key_attributes import IntakeAPIKeyAttributes
        from datadog_api_client.v2.model.intake_api_key_type import IntakeAPIKeyType

        return {
            "attributes": (IntakeAPIKeyAttributes,),
            "id": (str,),
            "type": (IntakeAPIKeyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: IntakeAPIKeyAttributes, id: str, type: IntakeAPIKeyType, **kwargs):
        """
        An intake API key resource.

        :param attributes: Attributes of an intake API key returned after successful authentication.
        :type attributes: IntakeAPIKeyAttributes

        :param id: A stable identifier for the intake key, scoped to the matched organization.
        :type id: str

        :param type: The resource type for an intake API key.
        :type type: IntakeAPIKeyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
