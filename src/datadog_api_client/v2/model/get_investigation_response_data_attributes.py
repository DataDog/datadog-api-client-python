# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.investigation_conclusion import InvestigationConclusion


class GetInvestigationResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.investigation_conclusion import InvestigationConclusion

        return {
            "conclusions": ([InvestigationConclusion],),
            "status": (str,),
            "title": (str,),
        }

    attribute_map = {
        "conclusions": "conclusions",
        "status": "status",
        "title": "title",
    }

    def __init__(self_, conclusions: List[InvestigationConclusion], status: str, title: str, **kwargs):
        """
        Attributes of the investigation.

        :param conclusions: The conclusions drawn from the investigation.
        :type conclusions: [InvestigationConclusion]

        :param status: The current status of the investigation.
        :type status: str

        :param title: The title of the investigation.
        :type title: str
        """
        super().__init__(kwargs)

        self_.conclusions = conclusions
        self_.status = status
        self_.title = title
