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


class ElasticCloudCcmSettingsUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "elastic_org_id": (str,),
        }

    attribute_map = {
        "elastic_org_id": "elastic_org_id",
    }

    def __init__(self_, elastic_org_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Partial Elastic Cloud CCM interface settings for updates.

        :param elastic_org_id: Your Elastic Cloud organization ID, found in your organization settings.
        :type elastic_org_id: str, optional
        """
        if elastic_org_id is not unset:
            kwargs["elastic_org_id"] = elastic_org_id
        super().__init__(kwargs)
