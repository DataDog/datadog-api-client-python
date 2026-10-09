# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.severity_override_result import SeverityOverrideResult


class SeverityOverrideResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_override_result import SeverityOverrideResult

        return {
            "warnings": ([SeverityOverrideResult],),
        }

    attribute_map = {
        "warnings": "warnings",
    }

    def __init__(self_, warnings: Union[List[SeverityOverrideResult], UnsetType] = unset, **kwargs):
        """
        Security findings skipped while processing the severity override request.

        :param warnings: Findings skipped because an automation rule set their severity.
        :type warnings: [SeverityOverrideResult], optional
        """
        if warnings is not unset:
            kwargs["warnings"] = warnings
        super().__init__(kwargs)
