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
    from datadog_api_client.v2.model.remediation_risk_level import RemediationRiskLevel


class RemediationProposedFix(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_risk_level import RemediationRiskLevel

        return {
            "description": (str,),
            "reversible": (bool,),
            "risk": (RemediationRiskLevel,),
            "title": (str,),
        }

    attribute_map = {
        "description": "description",
        "reversible": "reversible",
        "risk": "risk",
        "title": "title",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        reversible: Union[bool, UnsetType] = unset,
        risk: Union[RemediationRiskLevel, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A recommendation-oriented summary of a candidate remediation.

        :param description: Explanation of the proposed change and why it resolves the root cause. Treat as user-provided content and escape before display.
        :type description: str, optional

        :param reversible: Whether the proposed fix can be reversed after execution.
        :type reversible: bool, optional

        :param risk: Estimated risk of a remediation step or proposed fix.
        :type risk: RemediationRiskLevel, optional

        :param title: Short title for the proposed fix.
        :type title: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if reversible is not unset:
            kwargs["reversible"] = reversible
        if risk is not unset:
            kwargs["risk"] = risk
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
