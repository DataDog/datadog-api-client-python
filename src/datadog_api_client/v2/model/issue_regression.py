# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class IssueRegression(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "regressed_at": (datetime,),
            "regressed_at_version": (str,),
            "resolved_at": (datetime,),
        }

    attribute_map = {
        "regressed_at": "regressed_at",
        "regressed_at_version": "regressed_at_version",
        "resolved_at": "resolved_at",
    }

    def __init__(
        self_,
        regressed_at: datetime,
        resolved_at: datetime,
        regressed_at_version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Regression information for an issue that was previously resolved and then reopened.

        :param regressed_at: Timestamp when the issue was reopened (regressed).
        :type regressed_at: datetime

        :param regressed_at_version: Application version where the regression was observed.
        :type regressed_at_version: str, optional

        :param resolved_at: Timestamp when the issue was resolved before the regression.
        :type resolved_at: datetime
        """
        if regressed_at_version is not unset:
            kwargs["regressed_at_version"] = regressed_at_version
        super().__init__(kwargs)

        self_.regressed_at = regressed_at
        self_.resolved_at = resolved_at
