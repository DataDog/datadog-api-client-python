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
    from datadog_api_client.v2.model.experiments_bandit_v2_warning_code import ExperimentsBanditV2WarningCode


class ExperimentsBanditV2WarningDTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_v2_warning_code import ExperimentsBanditV2WarningCode

        return {
            "code": (ExperimentsBanditV2WarningCode,),
            "detail": (str,),
        }

    attribute_map = {
        "code": "code",
        "detail": "detail",
    }

    def __init__(self_, code: ExperimentsBanditV2WarningCode, detail: str, **kwargs):
        """
        A warning about the response that isn't an error.

        :param code: Code that identifies the warning. ``datadog_flag_configuration_omitted`` means the caller lacks feature flag or environment read permissions, so the response leaves out ``datadog_flag_configuration``.
        :type code: ExperimentsBanditV2WarningCode

        :param detail: Explanation of the warning.
        :type detail: str
        """
        super().__init__(kwargs)

        self_.code = code
        self_.detail = detail
