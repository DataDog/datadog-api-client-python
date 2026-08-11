# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ElasticCloudCcmSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "elastic_org_id": (str,),
        }

    attribute_map = {
        "elastic_org_id": "elastic_org_id",
    }

    def __init__(self_, elastic_org_id: str, **kwargs):
        """
        Elastic Cloud CCM interface settings.

        :param elastic_org_id: Your Elastic Cloud organization ID, found in your organization settings.
        :type elastic_org_id: str
        """
        super().__init__(kwargs)

        self_.elastic_org_id = elastic_org_id
