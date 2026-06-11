# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.network_health_insight_failure_type import NetworkHealthInsightFailureType
    from datadog_api_client.v2.model.network_health_insight_traffic_volume import NetworkHealthInsightTrafficVolume
    from datadog_api_client.v2.model.network_health_insight_category import NetworkHealthInsightCategory


class NetworkHealthInsightAttributes(ModelNormal):
    validations = {
        "failure_magnitude": {
            "inclusive_minimum": 0,
        },
        "failure_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
        "total_requests": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.network_health_insight_failure_type import NetworkHealthInsightFailureType
        from datadog_api_client.v2.model.network_health_insight_traffic_volume import NetworkHealthInsightTrafficVolume
        from datadog_api_client.v2.model.network_health_insight_category import NetworkHealthInsightCategory

        return {
            "account_id": (str,),
            "certificate_id": (str,),
            "certificate_lifetime_percent": (float,),
            "client_region": (str,),
            "client_service": (str,),
            "days_until_expiration": (int,),
            "dns_query": (str,),
            "dns_server": (str,),
            "domain_name": (str,),
            "failure_magnitude": (int,),
            "failure_rate": (float,),
            "failure_type": (NetworkHealthInsightFailureType,),
            "loadbalancer_id": (str,),
            "server_region": (str,),
            "server_service": (str,),
            "total_requests": (int,),
            "traffic_volume": (NetworkHealthInsightTrafficVolume,),
            "type": (NetworkHealthInsightCategory,),
        }

    attribute_map = {
        "account_id": "account_id",
        "certificate_id": "certificate_id",
        "certificate_lifetime_percent": "certificate_lifetime_percent",
        "client_region": "client_region",
        "client_service": "client_service",
        "days_until_expiration": "days_until_expiration",
        "dns_query": "dns_query",
        "dns_server": "dns_server",
        "domain_name": "domain_name",
        "failure_magnitude": "failure_magnitude",
        "failure_rate": "failure_rate",
        "failure_type": "failure_type",
        "loadbalancer_id": "loadbalancer_id",
        "server_region": "server_region",
        "server_service": "server_service",
        "total_requests": "total_requests",
        "traffic_volume": "traffic_volume",
        "type": "type",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        certificate_id: Union[str, UnsetType] = unset,
        certificate_lifetime_percent: Union[float, UnsetType] = unset,
        client_region: Union[str, UnsetType] = unset,
        client_service: Union[str, UnsetType] = unset,
        days_until_expiration: Union[int, UnsetType] = unset,
        dns_query: Union[str, UnsetType] = unset,
        dns_server: Union[str, UnsetType] = unset,
        domain_name: Union[str, UnsetType] = unset,
        failure_magnitude: Union[int, UnsetType] = unset,
        failure_rate: Union[float, UnsetType] = unset,
        failure_type: Union[NetworkHealthInsightFailureType, UnsetType] = unset,
        loadbalancer_id: Union[str, UnsetType] = unset,
        server_region: Union[str, UnsetType] = unset,
        server_service: Union[str, UnsetType] = unset,
        total_requests: Union[int, UnsetType] = unset,
        traffic_volume: Union[NetworkHealthInsightTrafficVolume, UnsetType] = unset,
        type: Union[NetworkHealthInsightCategory, UnsetType] = unset,
        **kwargs,
    ):
        """
        Detailed attributes of a network health insight.

        :param account_id: AWS account identifier where the certificate is located. Only set for ``tls-cert`` insights.
        :type account_id: str, optional

        :param certificate_id: ARN or identifier of the certificate. Only set for ``tls-cert`` insights.
        :type certificate_id: str, optional

        :param certificate_lifetime_percent: Percentage of the certificate's validity period that has elapsed, ranging from 0 to 100.
            Only set for ``tls-cert`` insights.
        :type certificate_lifetime_percent: float, optional

        :param client_region: AWS region where the client is located. Only set for ``tls-cert`` insights.
        :type client_region: str, optional

        :param client_service: Name of the service making the request (DNS query or TLS-secured connection).
            Set to ``N/A`` when the client service cannot be determined.
        :type client_service: str, optional

        :param days_until_expiration: Number of days remaining until the certificate expires. Negative values indicate the
            certificate has already expired. Only set for ``tls-cert`` insights.
        :type days_until_expiration: int, optional

        :param dns_query: Domain name that was being resolved when the DNS failure occurred. Only set for ``dns`` insights.
        :type dns_query: str, optional

        :param dns_server: DNS server that received the failing query. Only set for ``dns`` insights.
        :type dns_server: str, optional

        :param domain_name: Domain name covered by the certificate. Only set for ``tls-cert`` insights.
        :type domain_name: str, optional

        :param failure_magnitude: Count of failed events observed during the query window. Only set for ``dns`` , ``tcp`` ,
            and ``security-group`` insights.
        :type failure_magnitude: int, optional

        :param failure_rate: Percentage of requests that failed during the query window, ranging from 0 to 100.
            Only set for ``dns`` , ``tcp`` , and ``security-group`` insights.
        :type failure_rate: float, optional

        :param failure_type: Specific failure type within the insight category. For DNS insights: ``timeout`` , ``nxdomain`` ,
            ``servfail`` , or ``general_failure``. For TLS certificate insights: ``expired`` or ``expiring_soon``.
            For security group insights: ``denied``.
        :type failure_type: NetworkHealthInsightFailureType, optional

        :param loadbalancer_id: ARN of the load balancer using the certificate. Only set for ``tls-cert`` insights.
        :type loadbalancer_id: str, optional

        :param server_region: AWS region where the server or load balancer is located. Only set for ``tls-cert`` insights.
        :type server_region: str, optional

        :param server_service: Name of the target service the client was trying to reach.
        :type server_service: str, optional

        :param total_requests: Total number of requests observed during the query window. Provides context for
            ``failure_magnitude`` and ``failure_rate``. Only set for ``dns`` , ``tcp`` , and ``security-group`` insights.
        :type total_requests: int, optional

        :param traffic_volume: Network traffic volume metrics between the client and server services during the query window.
        :type traffic_volume: NetworkHealthInsightTrafficVolume, optional

        :param type: Category of network health insight. Indicates whether the insight relates to a DNS issue ( ``dns`` ),
            a TCP issue ( ``tcp`` ), a TLS certificate issue ( ``tls-cert`` ), or a security group denial ( ``security-group`` ).
        :type type: NetworkHealthInsightCategory, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if certificate_id is not unset:
            kwargs["certificate_id"] = certificate_id
        if certificate_lifetime_percent is not unset:
            kwargs["certificate_lifetime_percent"] = certificate_lifetime_percent
        if client_region is not unset:
            kwargs["client_region"] = client_region
        if client_service is not unset:
            kwargs["client_service"] = client_service
        if days_until_expiration is not unset:
            kwargs["days_until_expiration"] = days_until_expiration
        if dns_query is not unset:
            kwargs["dns_query"] = dns_query
        if dns_server is not unset:
            kwargs["dns_server"] = dns_server
        if domain_name is not unset:
            kwargs["domain_name"] = domain_name
        if failure_magnitude is not unset:
            kwargs["failure_magnitude"] = failure_magnitude
        if failure_rate is not unset:
            kwargs["failure_rate"] = failure_rate
        if failure_type is not unset:
            kwargs["failure_type"] = failure_type
        if loadbalancer_id is not unset:
            kwargs["loadbalancer_id"] = loadbalancer_id
        if server_region is not unset:
            kwargs["server_region"] = server_region
        if server_service is not unset:
            kwargs["server_service"] = server_service
        if total_requests is not unset:
            kwargs["total_requests"] = total_requests
        if traffic_volume is not unset:
            kwargs["traffic_volume"] = traffic_volume
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
