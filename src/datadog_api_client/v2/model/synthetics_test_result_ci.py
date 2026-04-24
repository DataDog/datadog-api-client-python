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
    from datadog_api_client.v2.model.synthetics_test_result_ci_pipeline import SyntheticsTestResultCIPipeline
    from datadog_api_client.v2.model.synthetics_test_result_ci_provider import SyntheticsTestResultCIProvider
    from datadog_api_client.v2.model.synthetics_test_result_ci_stage import SyntheticsTestResultCIStage


class SyntheticsTestResultCI(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_ci_pipeline import SyntheticsTestResultCIPipeline
        from datadog_api_client.v2.model.synthetics_test_result_ci_provider import SyntheticsTestResultCIProvider
        from datadog_api_client.v2.model.synthetics_test_result_ci_stage import SyntheticsTestResultCIStage

        return {
            "pipeline": (SyntheticsTestResultCIPipeline,),
            "provider": (SyntheticsTestResultCIProvider,),
            "stage": (SyntheticsTestResultCIStage,),
            "workspace_path": (str,),
        }

    attribute_map = {
        "pipeline": "pipeline",
        "provider": "provider",
        "stage": "stage",
        "workspace_path": "workspace_path",
    }

    def __init__(
        self_,
        pipeline: Union[SyntheticsTestResultCIPipeline, UnsetType] = unset,
        provider: Union[SyntheticsTestResultCIProvider, UnsetType] = unset,
        stage: Union[SyntheticsTestResultCIStage, UnsetType] = unset,
        workspace_path: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        CI information associated with the test result.

        :param pipeline: Details of the CI pipeline.
        :type pipeline: SyntheticsTestResultCIPipeline, optional

        :param provider: Details of the CI provider.
        :type provider: SyntheticsTestResultCIProvider, optional

        :param stage: Details of the CI stage.
        :type stage: SyntheticsTestResultCIStage, optional

        :param workspace_path: Path of the workspace that ran the CI job.
        :type workspace_path: str, optional
        """
        if pipeline is not unset:
            kwargs["pipeline"] = pipeline
        if provider is not unset:
            kwargs["provider"] = provider
        if stage is not unset:
            kwargs["stage"] = stage
        if workspace_path is not unset:
            kwargs["workspace_path"] = workspace_path
        super().__init__(kwargs)
