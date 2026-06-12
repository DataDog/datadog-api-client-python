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


class LLMObsPatternsConfigUpsertRequestAttributes(ModelNormal):
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
            "config_id": (str,),
            "evp_query": (str,),
            "hierarchy_depth": (int,),
            "integration_provider": (str,),
            "model_name": (str,),
            "name": (str,),
            "num_records": (int,),
            "sampling_ratio": (float,),
            "scope": (str,),
            "template": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "config_id": "config_id",
        "evp_query": "evp_query",
        "hierarchy_depth": "hierarchy_depth",
        "integration_provider": "integration_provider",
        "model_name": "model_name",
        "name": "name",
        "num_records": "num_records",
        "sampling_ratio": "sampling_ratio",
        "scope": "scope",
        "template": "template",
    }

    def __init__(
        self_,
        evp_query: str,
        hierarchy_depth: int,
        name: str,
        num_records: int,
        sampling_ratio: float,
        account_id: Union[str, UnsetType] = unset,
        config_id: Union[str, UnsetType] = unset,
        integration_provider: Union[str, UnsetType] = unset,
        model_name: Union[str, UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        template: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating an LLM Observability patterns configuration.

        :param account_id: Integration account ID for a bring-your-own-model configuration.
        :type account_id: str, optional

        :param config_id: The ID of an existing configuration to update. If omitted, a new configuration is created.
        :type config_id: str, optional

        :param evp_query: Query that selects the spans the patterns run analyzes.
        :type evp_query: str

        :param hierarchy_depth: Depth of the topic hierarchy to generate.
        :type hierarchy_depth: int

        :param integration_provider: Integration provider for a bring-your-own-model configuration.
        :type integration_provider: str, optional

        :param model_name: Model name for a bring-your-own-model configuration.
        :type model_name: str, optional

        :param name: Name of the configuration.
        :type name: str

        :param num_records: Maximum number of records to process for the run.
        :type num_records: int

        :param sampling_ratio: Fraction of matching spans to sample for the run.
        :type sampling_ratio: float

        :param scope: Scope of the configuration.
        :type scope: str, optional

        :param template: Template used to guide topic generation.
        :type template: str, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if config_id is not unset:
            kwargs["config_id"] = config_id
        if integration_provider is not unset:
            kwargs["integration_provider"] = integration_provider
        if model_name is not unset:
            kwargs["model_name"] = model_name
        if scope is not unset:
            kwargs["scope"] = scope
        if template is not unset:
            kwargs["template"] = template
        super().__init__(kwargs)

        self_.evp_query = evp_query
        self_.hierarchy_depth = hierarchy_depth
        self_.name = name
        self_.num_records = num_records
        self_.sampling_ratio = sampling_ratio
