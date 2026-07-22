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
    from datadog_api_client.v2.model.pup_bump_test_data_attributes import PupBumpTestDataAttributes
    from datadog_api_client.v2.model.pup_bump_test_type import PupBumpTestType


class PupBumpTestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pup_bump_test_data_attributes import PupBumpTestDataAttributes
        from datadog_api_client.v2.model.pup_bump_test_type import PupBumpTestType

        return {
            "attributes": (PupBumpTestDataAttributes,),
            "id": (str,),
            "type": (PupBumpTestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: PupBumpTestDataAttributes, id: str, type: PupBumpTestType, **kwargs):
        """
        Pup bump test resource data.

        :param attributes: Attributes of the pup bump test resource.
        :type attributes: PupBumpTestDataAttributes

        :param id: Pup bump test identifier.
        :type id: str

        :param type: Pup bump test resource type.
        :type type: PupBumpTestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
