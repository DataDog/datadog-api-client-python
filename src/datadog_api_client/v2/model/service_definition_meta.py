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
    from datadog_api_client.v2.model.service_definition_meta_warnings import ServiceDefinitionMetaWarnings


class ServiceDefinitionMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_definition_meta_warnings import ServiceDefinitionMetaWarnings

        return {
            "github_html_url": (str,),
            "ingested_schema_version": (str,),
            "ingestion_source": (str,),
            "last_modified_time": (str,),
            "origin": (str,),
            "origin_detail": (str,),
            "warnings": ([ServiceDefinitionMetaWarnings],),
        }

    attribute_map = {
        "github_html_url": "github-html-url",
        "ingested_schema_version": "ingested-schema-version",
        "ingestion_source": "ingestion-source",
        "last_modified_time": "last-modified-time",
        "origin": "origin",
        "origin_detail": "origin-detail",
        "warnings": "warnings",
    }

    def __init__(
        self_,
        github_html_url: Union[str, UnsetType] = unset,
        ingested_schema_version: Union[str, UnsetType] = unset,
        ingestion_source: Union[str, UnsetType] = unset,
        last_modified_time: Union[str, UnsetType] = unset,
        origin: Union[str, UnsetType] = unset,
        origin_detail: Union[str, UnsetType] = unset,
        warnings: Union[List[ServiceDefinitionMetaWarnings], UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about a service definition.

        :param github_html_url: GitHub HTML URL.
        :type github_html_url: str, optional

        :param ingested_schema_version: Ingestion schema version.
        :type ingested_schema_version: str, optional

        :param ingestion_source: Ingestion source of the service definition.
        :type ingestion_source: str, optional

        :param last_modified_time: Last modified time of the service definition.
        :type last_modified_time: str, optional

        :param origin: User defined origin of the service definition.
        :type origin: str, optional

        :param origin_detail: User defined origin's detail of the service definition.
        :type origin_detail: str, optional

        :param warnings: A list of schema validation warnings.
        :type warnings: [ServiceDefinitionMetaWarnings], optional
        """
        if github_html_url is not unset:
            kwargs["github_html_url"] = github_html_url
        if ingested_schema_version is not unset:
            kwargs["ingested_schema_version"] = ingested_schema_version
        if ingestion_source is not unset:
            kwargs["ingestion_source"] = ingestion_source
        if last_modified_time is not unset:
            kwargs["last_modified_time"] = last_modified_time
        if origin is not unset:
            kwargs["origin"] = origin
        if origin_detail is not unset:
            kwargs["origin_detail"] = origin_detail
        if warnings is not unset:
            kwargs["warnings"] = warnings
        super().__init__(kwargs)
