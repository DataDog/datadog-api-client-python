# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DeploymentGatesEvaluationResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "evaluation_id": (str,),
        }

    attribute_map = {
        "evaluation_id": "evaluation_id",
    }

    def __init__(self_, evaluation_id: str, **kwargs):
        """
        Attributes for a deployment gate evaluation response.

        :param evaluation_id: The unique identifier of the gate evaluation.
        :type evaluation_id: str
        """
        super().__init__(kwargs)

        self_.evaluation_id = evaluation_id
