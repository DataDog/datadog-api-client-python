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
    from datadog_api_client.v2.model.deployment_gate_evaluation_page import DeploymentGateEvaluationPage


class DeploymentGateEvaluationListMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gate_evaluation_page import DeploymentGateEvaluationPage

        return {
            "page": (DeploymentGateEvaluationPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: DeploymentGateEvaluationPage, **kwargs):
        """
        Pagination metadata.

        :param page: Cursor pagination information.
        :type page: DeploymentGateEvaluationPage
        """
        super().__init__(kwargs)

        self_.page = page
