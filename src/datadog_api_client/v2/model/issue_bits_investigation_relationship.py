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
    from datadog_api_client.v2.model.issue_bits_investigation_reference import IssueBitsInvestigationReference


class IssueBitsInvestigationRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_bits_investigation_reference import IssueBitsInvestigationReference

        return {
            "data": (IssueBitsInvestigationReference,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IssueBitsInvestigationReference, **kwargs):
        """
        Bits AI investigation linked to the issue, returned when ``bits_investigation`` is requested
        in the ``include`` query parameter.

        :param data: The Bits AI investigation linked to the issue.
        :type data: IssueBitsInvestigationReference
        """
        super().__init__(kwargs)

        self_.data = data
