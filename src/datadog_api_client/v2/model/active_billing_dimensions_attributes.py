# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class ActiveBillingDimensionsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "month": (datetime,),
            "values": ([str],),
        }

    attribute_map = {
        "month": "month",
        "values": "values",
    }

    def __init__(
        self_, month: Union[datetime, UnsetType] = unset, values: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        List of active billing dimensions.

        :param month: Datetime in ISO-8601 format, UTC, precise to hour: ``[YYYY-MM-DDThh]``.
        :type month: datetime, optional

        :param values: List of active billing dimensions. Example: ``[infra_host, apm_host, serverless_infra]``.
        :type values: [str], optional
        """
        if month is not unset:
            kwargs["month"] = month
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
