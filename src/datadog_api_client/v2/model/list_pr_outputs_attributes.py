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
    from datadog_api_client.v2.model.pr_output import PROutput


class ListPROutputsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pr_output import PROutput

        return {
            "pr_outputs": ([PROutput],),
        }

    attribute_map = {
        "pr_outputs": "pr_outputs",
    }

    def __init__(self_, pr_outputs: List[PROutput], **kwargs):
        """
        Attributes of a PR outputs response.

        :param pr_outputs: The list of pull requests created by the workflow execution.
        :type pr_outputs: [PROutput]
        """
        super().__init__(kwargs)

        self_.pr_outputs = pr_outputs
