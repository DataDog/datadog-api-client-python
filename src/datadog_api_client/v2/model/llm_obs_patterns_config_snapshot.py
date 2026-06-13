# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class LLMObsPatternsConfigSnapshot(ModelNormal):
    validations = {
        "hierarchy_depth": {
            "inclusive_maximum": 2147483647,
        },
        "num_records": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "evp_query": (str,),
            "hierarchy_depth": (int,),
            "integration_provider": (str,),
            "model_name": (str,),
            "num_records": (int,),
            "sampling_ratio": (float,),
        }

    attribute_map = {
        "account_id": "account_id",
        "evp_query": "evp_query",
        "hierarchy_depth": "hierarchy_depth",
        "integration_provider": "integration_provider",
        "model_name": "model_name",
        "num_records": "num_records",
        "sampling_ratio": "sampling_ratio",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        evp_query: Union[str, UnsetType] = unset,
        hierarchy_depth: Union[int, UnsetType] = unset,
        integration_provider: Union[str, UnsetType] = unset,
        model_name: Union[str, UnsetType] = unset,
        num_records: Union[int, UnsetType] = unset,
        sampling_ratio: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Snapshot of the configuration used for a patterns run.

        :param account_id: Integration account ID used for a bring-your-own-model run.
        :type account_id: str, optional

        :param evp_query: Query that selected the spans for the run.
        :type evp_query: str, optional

        :param hierarchy_depth: Depth of the topic hierarchy generated.
        :type hierarchy_depth: int, optional

        :param integration_provider: Integration provider used for a bring-your-own-model run.
        :type integration_provider: str, optional

        :param model_name: Model name used for a bring-your-own-model run.
        :type model_name: str, optional

        :param num_records: Maximum number of records processed for the run.
        :type num_records: int, optional

        :param sampling_ratio: Fraction of matching spans sampled for the run.
        :type sampling_ratio: float, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if evp_query is not unset:
            kwargs["evp_query"] = evp_query
        if hierarchy_depth is not unset:
            kwargs["hierarchy_depth"] = hierarchy_depth
        if integration_provider is not unset:
            kwargs["integration_provider"] = integration_provider
        if model_name is not unset:
            kwargs["model_name"] = model_name
        if num_records is not unset:
            kwargs["num_records"] = num_records
        if sampling_ratio is not unset:
            kwargs["sampling_ratio"] = sampling_ratio
        super().__init__(kwargs)
