# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class UsageSummaryAvailableFieldsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "date_fields": ([str],),
            "date_org_fields": ([str],),
            "response_fields": ([str],),
        }

    attribute_map = {
        "date_fields": "date_fields",
        "date_org_fields": "date_org_fields",
        "response_fields": "response_fields",
    }

    def __init__(
        self_,
        date_fields: Union[List[str], UnsetType] = unset,
        date_org_fields: Union[List[str], UnsetType] = unset,
        response_fields: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The lists of field names returned by ``GET /api/v1/usage/summary`` at each
        of its three response levels. Each list contains every key the data endpoint
        emits—both typed fields declared in the OpenAPI spec and untyped keys
        exposed through ``additionalProperties``.

        :param date_fields: Sorted list of every key returned inside each ``UsageSummaryDate``
            entry of ``usage[]`` (typed fields and ``additionalProperties`` keys
            combined).
        :type date_fields: [str], optional

        :param date_org_fields: Sorted list of every key returned inside each ``UsageSummaryDateOrg``
            entry of ``usage[].orgs[]`` (typed fields and ``additionalProperties``
            keys combined).
        :type date_org_fields: [str], optional

        :param response_fields: Sorted list of every key returned as a direct property of
            ``UsageSummaryResponse`` (typed fields and ``additionalProperties``
            keys combined).
        :type response_fields: [str], optional
        """
        if date_fields is not unset:
            kwargs["date_fields"] = date_fields
        if date_org_fields is not unset:
            kwargs["date_org_fields"] = date_org_fields
        if response_fields is not unset:
            kwargs["response_fields"] = response_fields
        super().__init__(kwargs)
