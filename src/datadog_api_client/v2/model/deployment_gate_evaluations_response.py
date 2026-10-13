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
    from datadog_api_client.v2.model.deployment_gate_evaluation_data import DeploymentGateEvaluationData
    from datadog_api_client.v2.model.deployment_gate_evaluation_list_meta import DeploymentGateEvaluationListMeta


class DeploymentGateEvaluationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gate_evaluation_data import DeploymentGateEvaluationData
        from datadog_api_client.v2.model.deployment_gate_evaluation_list_meta import DeploymentGateEvaluationListMeta

        return {
            "data": ([DeploymentGateEvaluationData],),
            "meta": (DeploymentGateEvaluationListMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[DeploymentGateEvaluationData], meta: DeploymentGateEvaluationListMeta, **kwargs):
        """
        Paginated deployment gate evaluations.

        :param data:
        :type data: [DeploymentGateEvaluationData]

        :param meta: Pagination metadata.
        :type meta: DeploymentGateEvaluationListMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
