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
    from datadog_api_client.v2.model.case_insight_type import CaseInsightType


class CaseInsight(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_insight_type import CaseInsightType

        return {
            "ref": (str,),
            "resource_id": (str,),
            "type": (CaseInsightType,),
        }

    attribute_map = {
        "ref": "ref",
        "resource_id": "resource_id",
        "type": "type",
    }

    def __init__(self_, ref: str, resource_id: str, type: CaseInsightType, **kwargs):
        """
        A reference to an external Datadog resource that provides investigative context for a case, such as a security signal, monitor alert, error tracking issue, or incident.

        :param ref: The URL path or deep link to the insight resource within Datadog (for example, ``/monitors/12345?q=total`` ).
        :type ref: str

        :param resource_id: The unique identifier of the referenced Datadog resource (for example, a monitor ID, incident ID, or signal ID).
        :type resource_id: str

        :param type: The type of Datadog resource linked to the case as contextual evidence. Each type corresponds to a different Datadog product signal (for example, a security finding, a monitor alert, or an incident).
        :type type: CaseInsightType
        """
        super().__init__(kwargs)

        self_.ref = ref
        self_.resource_id = resource_id
        self_.type = type
