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
    from datadog_api_client.v2.model.estimation import Estimation


class ComponentRecommendation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.estimation import Estimation

        return {
            "estimation": (Estimation,),
        }

    attribute_map = {
        "estimation": "estimation",
    }

    def __init__(self_, estimation: Estimation, **kwargs):
        """
        Resource recommendation for a single Spark component (driver or executor). Contains estimation data used to patch Spark job specs.

        :param estimation: Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.
        :type estimation: Estimation
        """
        super().__init__(kwargs)

        self_.estimation = estimation
