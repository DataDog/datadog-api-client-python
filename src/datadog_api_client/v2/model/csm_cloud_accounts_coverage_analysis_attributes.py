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
    from datadog_api_client.v2.model.csm_coverage_analysis import CsmCoverageAnalysis


class CsmCloudAccountsCoverageAnalysisAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_coverage_analysis import CsmCoverageAnalysis

        return {
            "aws_coverage": (CsmCoverageAnalysis,),
            "azure_coverage": (CsmCoverageAnalysis,),
            "gcp_coverage": (CsmCoverageAnalysis,),
            "org_id": (int,),
            "total_coverage": (CsmCoverageAnalysis,),
        }

    attribute_map = {
        "aws_coverage": "aws_coverage",
        "azure_coverage": "azure_coverage",
        "gcp_coverage": "gcp_coverage",
        "org_id": "org_id",
        "total_coverage": "total_coverage",
    }

    def __init__(
        self_,
        aws_coverage: Union[CsmCoverageAnalysis, UnsetType] = unset,
        azure_coverage: Union[CsmCoverageAnalysis, UnsetType] = unset,
        gcp_coverage: Union[CsmCoverageAnalysis, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        total_coverage: Union[CsmCoverageAnalysis, UnsetType] = unset,
        **kwargs,
    ):
        """
        CSM Cloud Accounts Coverage Analysis attributes.

        :param aws_coverage: CSM Coverage Analysis.
        :type aws_coverage: CsmCoverageAnalysis, optional

        :param azure_coverage: CSM Coverage Analysis.
        :type azure_coverage: CsmCoverageAnalysis, optional

        :param gcp_coverage: CSM Coverage Analysis.
        :type gcp_coverage: CsmCoverageAnalysis, optional

        :param org_id: The ID of your organization.
        :type org_id: int, optional

        :param total_coverage: CSM Coverage Analysis.
        :type total_coverage: CsmCoverageAnalysis, optional
        """
        if aws_coverage is not unset:
            kwargs["aws_coverage"] = aws_coverage
        if azure_coverage is not unset:
            kwargs["azure_coverage"] = azure_coverage
        if gcp_coverage is not unset:
            kwargs["gcp_coverage"] = gcp_coverage
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if total_coverage is not unset:
            kwargs["total_coverage"] = total_coverage
        super().__init__(kwargs)
