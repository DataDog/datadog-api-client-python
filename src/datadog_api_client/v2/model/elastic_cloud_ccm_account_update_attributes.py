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
    from datadog_api_client.v2.model.elastic_cloud_ccm_authentication import ElasticCloudCcmAuthentication
    from datadog_api_client.v2.model.elastic_cloud_ccm_dataflow import ElasticCloudCcmDataflow
    from datadog_api_client.v2.model.elastic_cloud_ccm_settings_update import ElasticCloudCcmSettingsUpdate
    from datadog_api_client.v2.model.elastic_cloud_ccm_token_auth import ElasticCloudCcmTokenAuth


class ElasticCloudCcmAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_ccm_authentication import ElasticCloudCcmAuthentication
        from datadog_api_client.v2.model.elastic_cloud_ccm_dataflow import ElasticCloudCcmDataflow
        from datadog_api_client.v2.model.elastic_cloud_ccm_settings_update import ElasticCloudCcmSettingsUpdate

        return {
            "authentication": (ElasticCloudCcmAuthentication,),
            "dataflows": ([ElasticCloudCcmDataflow],),
            "name": (str,),
            "settings": (ElasticCloudCcmSettingsUpdate,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[ElasticCloudCcmAuthentication, ElasticCloudCcmTokenAuth, UnsetType] = unset,
        dataflows: Union[List[ElasticCloudCcmDataflow], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[ElasticCloudCcmSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Updatable attributes of an Elastic Cloud CCM account. Every field is optional; only the fields provided are changed.

        :param authentication: Authentication methods supported by the Elastic Cloud CCM interface. Exactly one is set, selected by its ``type``.
        :type authentication: ElasticCloudCcmAuthentication, optional

        :param dataflows: Dataflows for the Elastic Cloud CCM interface.
        :type dataflows: [ElasticCloudCcmDataflow], optional

        :param name: Human-readable name of the account.
        :type name: str, optional

        :param settings: Partial Elastic Cloud CCM interface settings for updates.
        :type settings: ElasticCloudCcmSettingsUpdate, optional
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        if name is not unset:
            kwargs["name"] = name
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
