# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OpsgenieServiceCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType

        return {
            "custom_url": (str,),
            "name": (str,),
            "opsgenie_api_key": (str,),
            "region": (OpsgenieServiceRegionType,),
        }

    attribute_map = {
        "custom_url": "custom_url",
        "name": "name",
        "opsgenie_api_key": "opsgenie_api_key",
        "region": "region",
    }

    def __init__(self, name, opsgenie_api_key, region, *args, **kwargs):
        """
        The Opsgenie service attributes for a create request.

        :param custom_url: The custom URL for a custom region.
        :type custom_url: str, optional

        :param name: The name for the Opsgenie service.
        :type name: str

        :param opsgenie_api_key: The Opsgenie API key for your Opsgenie service.
        :type opsgenie_api_key: str

        :param region: The region for the Opsgenie service.
        :type region: OpsgenieServiceRegionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.name = name
        self.opsgenie_api_key = opsgenie_api_key
        self.region = region

    @classmethod
    def _from_openapi_data(cls, name, opsgenie_api_key, region, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(OpsgenieServiceCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.name = name
        self.opsgenie_api_key = opsgenie_api_key
        self.region = region
        return self
