from typing import List, Optional

from pydantic import BaseModel

from ..base_model import BaseResponseModel


class CustomerBillingConfiguration(BaseModel):
    invoice_grace_period: Optional[int]
    payment_provider: Optional[str]
    provider_customer_id: Optional[str]
    vat_rate: Optional[float]
    sync: Optional[bool]
    sync_with_provider: Optional[bool]
    document_locale: Optional[str]


class Metadata(BaseModel):
    lago_id: Optional[str]
    key: Optional[str]
    value: Optional[str]
    display_in_invoice: Optional[bool]


class MetadataList(BaseModel):
    __root__: List[Metadata]


class Customer(BaseModel):
    external_id: str
    address_line1: Optional[str]
    address_line2: Optional[str]
    city: Optional[str]
    country: Optional[str]
    currency: Optional[str]
    email: Optional[str]
    legal_name: Optional[str]
    legal_number: Optional[str]
    logo_url: Optional[str]
    name: str
    phone: Optional[str]
    state: Optional[str]
    timezone: Optional[str]
    url: Optional[str]
    zipcode: Optional[str]
    metadata: Optional[MetadataList]
    billing_configuration: Optional[CustomerBillingConfiguration]


class CustomerResponse(BaseResponseModel):
    lago_id: str
    external_id: str
    address_line1: Optional[str]
    address_line2: Optional[str]
    city: Optional[str]
    country: Optional[str]
    currency: Optional[str]
    email: Optional[str]
    created_at: str
    legal_name: Optional[str]
    legal_number: Optional[str]
    logo_url: Optional[str]
    name: str
    phone: Optional[str]
    state: Optional[str]
    timezone: Optional[str]
    applicable_timezone: str
    url: Optional[str]
    zipcode: Optional[str]
    metadata: Optional[MetadataList]
    billing_configuration: Optional[CustomerBillingConfiguration]
