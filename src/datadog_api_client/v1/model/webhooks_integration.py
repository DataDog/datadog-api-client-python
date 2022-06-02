# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class WebhooksIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.webhooks_integration_encoding import WebhooksIntegrationEncoding

        return {
            "custom_headers": (str, none_type),
            "encode_as": (WebhooksIntegrationEncoding,),
            "name": (str,),
            "payload": (str, none_type),
            "url": (str,),
        }

    attribute_map = {
        "custom_headers": "custom_headers",
        "encode_as": "encode_as",
        "name": "name",
        "payload": "payload",
        "url": "url",
    }

    def __init__(self, name, url, *args, **kwargs):
        """
        Datadog-Webhooks integration.

        :param custom_headers: If ``null`` , uses no header.
            If given a JSON payload, these will be headers attached to your webhook.
        :type custom_headers: str, none_type, optional

        :param encode_as: Encoding type. Can be given either ``json`` or ``form``.
        :type encode_as: WebhooksIntegrationEncoding, optional

        :param name: The name of the webhook. It corresponds with ``<WEBHOOK_NAME>``.
            Learn more on how to use it in
            `monitor notifications <https://docs.datadoghq.com/monitors/notify>`_.
        :type name: str

        :param payload: If ``null`` , uses the default payload.
            If given a JSON payload, the webhook returns the payload
            specified by the given payload.
            `Webhooks variable usage <https://docs.datadoghq.com/integrations/webhooks/#usage>`_.
        :type payload: str, none_type, optional

        :param url: URL of the webhook.
        :type url: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.name = name
        self.url = url

    @classmethod
    def _from_openapi_data(cls, name, url, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WebhooksIntegration, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.name = name
        self.url = url
        return self
