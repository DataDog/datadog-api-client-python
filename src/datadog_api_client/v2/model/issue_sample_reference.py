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
    from datadog_api_client.v2.model.issue_sample_type import IssueSampleType


class IssueSampleReference(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_sample_type import IssueSampleType

        return {
            "id": (str,),
            "type": (IssueSampleType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: IssueSampleType, **kwargs):
        """
        A curated error sample of the issue.

        :param id: Sample identifier.
        :type id: str

        :param type: Type of the object.
        :type type: IssueSampleType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
